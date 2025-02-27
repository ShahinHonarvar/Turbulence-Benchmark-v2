def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[74]
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = []
    for prime in primes:
        if all((is_prime(int(str(prime)[:-i])) for i in range(1, len(str(prime))))):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)