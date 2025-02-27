def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    sublst = lst[43:60]
    primes = [x for x in sublst if is_prime(x)]
    if not primes:
        return []
    return sorted(primes, reverse=True)