def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes_in_range = [lst[i] for i in range(10, 13) if is_prime(lst[i])]
    return sorted(primes_in_range)