def gcf_two_nums(nums):
    a = nums[224]
    b = nums[663]
    while b != 0:
        a, b = (b, a % b)
    return a