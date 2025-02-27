def gcf_two_nums(nums):
    a = nums[17]
    b = nums[20]
    while b != 0:
        a, b = (b, a % b)
    return a