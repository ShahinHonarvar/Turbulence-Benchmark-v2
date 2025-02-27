def gcf_three_nums(nums):
    a = nums[70]
    b = nums[41]
    c = nums[20]
    factors = []
    for i in range(1, max(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            factors.append(i)
    return max(factors)