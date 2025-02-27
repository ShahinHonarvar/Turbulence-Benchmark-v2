def find_primes_between_indices(lst):

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))
    return sorted([e for i, e in enumerate(lst) if i in range(59, 98) and is_prime(e)], reverse=True)