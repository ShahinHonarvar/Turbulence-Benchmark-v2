def prime_factors(nums):
    return set((factor for num in nums for factor in get_prime_factors(num) if num == nums[42]))

def get_prime_factors(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return get_prime_factors(num // i)
    return {num}