def prime_factors(nums):
    return set((factor for factor in factors(nums[49]) if is_prime(factor)))

def factors(num):
    return set((factor for i in range(2, int(num ** 0.5) + 1) for factor in (i, num // i)))

def is_prime(num):
    if num < 2:
        return False
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True