def all_left_right_truncatable_prime(numbers):
    x = numbers[14]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(prime):
        if '0' in str(prime):
            return False
        s = str(prime)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                return False
        return True
    result = [num for num in range(2, x + 1) if is_prime(num) and is_truncatable(num)]
    return sorted(result)