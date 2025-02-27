def gcf_two_nums(nums):
    a = nums[56]
    b = nums[54]
    while b != 0:
        a, b = (b, a % b)
    return a