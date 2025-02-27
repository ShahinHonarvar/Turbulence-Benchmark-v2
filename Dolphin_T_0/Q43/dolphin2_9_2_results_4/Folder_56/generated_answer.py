def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in lst[40:69] if is_prime(i)], reverse=True) or []