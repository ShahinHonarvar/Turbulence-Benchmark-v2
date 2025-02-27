def prime_factors(nums):
    num = nums[23]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            num //= i
        else:
            i += 1
    if num > 1:
        factors.add(num)
    return factors