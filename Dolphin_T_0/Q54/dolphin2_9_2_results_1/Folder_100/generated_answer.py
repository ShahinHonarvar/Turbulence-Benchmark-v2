def all_right_truncatable_prime(numbers):
    x = numbers[26]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    primes = [n for n in range(1, x) if is_prime(n)]
    right_truncatable_primes = [n for n in primes if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes)