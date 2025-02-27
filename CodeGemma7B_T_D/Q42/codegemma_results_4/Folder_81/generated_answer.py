def prime_factors(nums):
    return {factor for factor in factors(nums[20]) if is_prime(factor)}

def factors(n):
    return set((factor for factor in range(2, 1 + int(n ** 0.5)) if not n % factor))

def is_prime(n):
    return all((n % factor for factor in range(2, 1 + int(n ** 0.5))))