def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[0]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result