def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                return False
        return True
    primes = [num for num in lst[31:68] if is_prime(num)]
    return sorted(primes, reverse=True)