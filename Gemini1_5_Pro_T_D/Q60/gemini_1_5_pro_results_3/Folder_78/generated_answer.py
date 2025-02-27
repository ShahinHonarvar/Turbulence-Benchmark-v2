def all_left_right_truncatable_prime(numbers):
    x = numbers[23]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:len(s) - i])):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result