def all_left_right_truncatable_prime(numbers):
    x = numbers[49]

    def is_left_right_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        if n < 100:
            return all((n % i for i in range(2, int(n ** 0.5) + 1)))
        s = str(n)
        for i in range(1, len(s)):
            if not all((int(s[i:]) % j for j in range(2, int(int(s[i:]) ** 0.5) + 1))):
                return False
            if not all((int(s[:-i]) % j for j in range(2, int(int(s[:-i]) ** 0.5) + 1))):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])