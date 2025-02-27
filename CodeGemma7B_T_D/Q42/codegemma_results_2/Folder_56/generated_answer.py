def prime_factors(nums):
    p_factors = set()
    val = nums[60]
    if val == 1:
        return p_factors
    div = 2
    while val > 1:
        if val % div == 0:
            p_factors.add(div)
            while val % div == 0:
                val //= div
        div += 1
    return p_factors