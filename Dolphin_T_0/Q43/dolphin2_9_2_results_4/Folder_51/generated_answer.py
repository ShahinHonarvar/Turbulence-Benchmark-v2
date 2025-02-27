def find_primes_between_indices(nums):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [x for x in nums[14:69] if is_prime(x)]
    if len(primes) == 0:
        return []
    else:
        return sorted(primes, reverse=True)