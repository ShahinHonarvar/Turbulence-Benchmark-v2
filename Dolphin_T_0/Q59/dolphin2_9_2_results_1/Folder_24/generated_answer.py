def all_left_truncatable_prime(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[65]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if is_truncatable(i)]
    return sorted(left_truncatable_primes, reverse=True)