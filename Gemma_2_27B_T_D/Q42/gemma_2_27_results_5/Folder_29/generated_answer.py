def prime_factors(nums):
    n = nums[19]
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors