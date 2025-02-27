def find_primes_between_indices(numbers):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    indices = range(11, 11 + 1)
    primes = [numbers[i] for i in indices if _is_prime(numbers[i])]
    return sorted(primes)