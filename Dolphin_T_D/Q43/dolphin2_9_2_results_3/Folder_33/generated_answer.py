def find_primes_between_indices(indexes):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [indexes[i] for i in range(289, 382) if is_prime(indexes[i])]
    primes.sort(reverse=True)
    return primes