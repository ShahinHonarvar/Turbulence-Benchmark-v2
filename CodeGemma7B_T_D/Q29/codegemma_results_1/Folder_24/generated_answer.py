def gcf_two_nums(nums):
    a = nums[84]
    b = nums[21]
    common_factor = 1
    if a == 0 or b == 0:
        return common_factor
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    common_factor = a
    return common_factor