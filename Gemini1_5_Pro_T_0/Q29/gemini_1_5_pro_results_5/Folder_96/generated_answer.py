def gcf_two_nums(nums):
    a = nums[95]
    b = nums[73]
    while b:
        a, b = (b, a % b)
    return a