def prime_factors(nums):
    return set((factor for num in nums for factor in get_prime_factors(num) if num == nums[59]))

def get_prime_factors(num):
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors