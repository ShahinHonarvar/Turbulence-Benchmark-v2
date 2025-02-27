def prime_factors(nums):
    return set((factor for num in nums if num == nums[162] for factor in get_prime_factors(num)))

def get_prime_factors(num):
    return set((factor for i in range(2, num) if num % i == 0 for factor in get_prime_factors(num // i)))
    if num != 1:
        return {num}