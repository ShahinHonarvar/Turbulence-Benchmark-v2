def all_left_truncatable_prime(numbers):
    x = numbers[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    left_truncatable_primes = [n for n in range(2, x) if '0' not in str(n) and is_prime(n) and is_left_truncatable(n)]
    return sorted(left_truncatable_primes, reverse=True)