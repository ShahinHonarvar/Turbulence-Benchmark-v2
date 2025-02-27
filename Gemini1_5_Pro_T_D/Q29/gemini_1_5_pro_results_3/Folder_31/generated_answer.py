def gcf_two_nums(nums):
    a = nums[87]
    b = nums[95]
    while b:
        a, b = (b, a % b)
    return a