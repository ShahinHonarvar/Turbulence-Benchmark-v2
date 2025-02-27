def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                return False
        return True
    return sorted([num for num in lst[24:73] if is_prime(num)])