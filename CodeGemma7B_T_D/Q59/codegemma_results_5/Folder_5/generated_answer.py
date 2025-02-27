def all_left_truncatable_prime(t):
    x = t[55]

    def left_truncatable_prime(n):
        if n % 2 == 0 or '0' in str(n) or any((str(n).startswith(str(i)) and (not prime(int(str(n)[len(str(i)):]))) for i in range(1, n // 2 + 1))):
            return False
        return True

    def prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in range(2, x) if left_truncatable_prime(i)])