def find_primes_between_indices(lst):

    def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return n > 1 and d * d > n
    return sorted([i for i in lst[14:74] if is_prime(i)], reverse=True)