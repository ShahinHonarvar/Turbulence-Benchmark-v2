def prime_factors(nums):
    return factors(nums[74])

def factors(n):
    result = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    result.discard(n)
    return result