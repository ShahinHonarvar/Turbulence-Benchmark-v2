def gcf_two_nums(nums):
    a = nums[0]
    b = nums[1]
    while b != 0:
        a, b = (b, a % b)
    return a