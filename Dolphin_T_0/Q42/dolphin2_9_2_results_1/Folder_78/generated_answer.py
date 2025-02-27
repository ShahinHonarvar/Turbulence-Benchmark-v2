def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for factor in prime_factors(nums[91] * nums[91]) if is_prime(factor)))