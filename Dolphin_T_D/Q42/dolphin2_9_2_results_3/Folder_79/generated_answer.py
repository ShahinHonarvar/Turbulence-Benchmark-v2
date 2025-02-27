def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    return set((i for i in range(2, nums[63]) if nums[63] % i == 0 and is_prime(i)))