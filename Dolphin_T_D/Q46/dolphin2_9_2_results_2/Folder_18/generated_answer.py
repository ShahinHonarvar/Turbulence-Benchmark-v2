def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    factors = [i for i in range(1, min(a, b, c) + 1) if a % i == b % i == c % i == 0]
    return max(factors)