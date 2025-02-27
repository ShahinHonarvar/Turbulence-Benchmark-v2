def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        while n > 0:
            if n < 2 or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
                return False
            n //= 10
        return True
    x = numbers[618]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    left_truncatable_primes.sort()
    return left_truncatable_primes