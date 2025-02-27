def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes_in_range = [lst[i] for i in range(24, 33) if is_prime(lst[i])]
    primes_in_range.sort(reverse=True)
    return primes_in_range