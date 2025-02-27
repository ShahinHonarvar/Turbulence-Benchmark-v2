def prime_factors(nums):
    return {**set(factors(nums[28]))}

def factors(n):
    i, factors = (2, set())
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors