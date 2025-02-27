def prime_factors(nums):
    n = nums[27]
    i = 2
    factors = set()
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return factors