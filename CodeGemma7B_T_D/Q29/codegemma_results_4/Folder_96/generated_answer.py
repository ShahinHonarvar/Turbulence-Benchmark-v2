def gcf_two_nums(nums):
    a = nums[95]
    b = nums[73]
    if a == 0:
        return b
    while b != 0:
        t = b
        b = a % b
        a = t
    return a