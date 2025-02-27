def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(prime):
        s = str(prime)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = numbers[91]
    result = []
    for n in range(11, x + 1):
        if '0' in str(n):
            continue
        if is_prime(n) and is_left_right_truncatable(n):
            result.append(n)
    return result