def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [nums[i] for i in range(19, 91) if is_prime(nums[i])]
    return sorted(primes, reverse=True)