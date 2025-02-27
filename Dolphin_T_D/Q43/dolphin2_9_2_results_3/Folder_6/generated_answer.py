def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    indices = range(89, 94)
    prime_numbers = [num for index, num in enumerate(lst) if index in indices and is_prime(num)]
    return sorted(prime_numbers, reverse=True) or []