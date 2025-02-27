def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [numbers[i] for i in range(87, 90) if is_prime(numbers[i])]
    return sorted(primes)