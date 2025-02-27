def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = [numbers[i] for i in range(131, 816) if is_prime(numbers[i])]
    return sorted(prime_numbers, reverse=True)