def find_primes_between_indices(list_nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes_between = [n for n in list_nums[23:76] if is_prime(n)]
    return sorted(primes_between, reverse=True)