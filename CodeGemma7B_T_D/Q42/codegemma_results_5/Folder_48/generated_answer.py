def prime_factors(nums):
    return {x for x in nums[247] if prime(x)}

def prime(n):
    if n <= 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True