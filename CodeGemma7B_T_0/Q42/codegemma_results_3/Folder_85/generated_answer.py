def prime_factors(nums):
    return set((factor for num in nums for factor in get_prime_factors(num) if num == nums[23]))

def get_prime_factors(num):
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    if num > 1:
        factors.add(num)
    return factors