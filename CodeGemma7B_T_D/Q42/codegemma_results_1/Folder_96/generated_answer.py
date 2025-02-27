def prime_factors(nums):
    factors = set()
    num = nums[47]
    i = 2
    while i * i <= num:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    if num > 1:
        factors.add(num)
    return factors