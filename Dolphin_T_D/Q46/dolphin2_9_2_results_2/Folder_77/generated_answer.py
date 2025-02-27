def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    factors = set()
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)