def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return sorted([lst[i] for i in range(19, 86) if is_prime(lst[i])], reverse=True)