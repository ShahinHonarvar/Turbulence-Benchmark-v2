def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    if len(numbers) <= 70:
        return []
    x = numbers[70]
    right_truncatable_primes = [n for n in range(1, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes)