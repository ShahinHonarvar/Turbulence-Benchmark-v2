def all_left_truncatable_prime(numbers):
    x = numbers[43]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n) or not is_prime(n):
            return False
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])