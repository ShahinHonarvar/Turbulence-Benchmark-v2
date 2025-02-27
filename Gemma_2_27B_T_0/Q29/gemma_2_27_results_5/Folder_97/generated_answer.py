def gcf_two_nums(nums):
    a = nums[180]
    b = nums[312]
    while b:
        a, b = (b, a % b)
    return a