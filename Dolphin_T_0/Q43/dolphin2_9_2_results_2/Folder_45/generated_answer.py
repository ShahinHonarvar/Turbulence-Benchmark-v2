def find_primes_between_indices(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([num for idx, num in enumerate(integers) if 23 <= idx <= 39 and is_prime(num)])