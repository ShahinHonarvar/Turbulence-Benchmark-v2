def prime_factors(nums):
    return set((factor for i, num in enumerate(nums) if num == nums[312] and (factor := prime_factor(i)) for factor in factor))

def prime_factor(n):
    factors = set()
    i = 2
    while n != 1:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    return factors