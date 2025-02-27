def prime_factors(nums):
    return set((factor for num in nums for factor in range(2, num + 1) if num % factor == 0 and is_prime(factor)))

def is_prime(num):
    if num <= 1:
        return False
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True