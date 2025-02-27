def prime_factors(nums):
    return set(factors(nums[8]))

def factors(n):
    result = set([1, n])
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.add(i)
            result.add(n // i)
        i += 1
    return result