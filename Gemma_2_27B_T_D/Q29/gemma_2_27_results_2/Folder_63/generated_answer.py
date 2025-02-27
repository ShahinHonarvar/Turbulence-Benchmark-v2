def gcf_two_nums(nums):
    a = nums[21]
    b = nums[17]
    while b:
        a, b = (b, a % b)
    return a