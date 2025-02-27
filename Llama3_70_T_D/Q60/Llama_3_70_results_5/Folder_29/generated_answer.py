def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return is_prime(int(s[1:])) and is_prime(int(s[:-1]))
    x = numbers[55]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    result.sort(reverse=True)
    return result