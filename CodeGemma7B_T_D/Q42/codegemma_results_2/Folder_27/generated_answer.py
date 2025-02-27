def prime_factors(nums):
    return set((factorize(num) for num in nums[56]))

def factorize(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return {i}.union(factorize(n // i))
    return {n}