def gcf_two_nums(nums):
    if len(nums) > 51:
        return 0
    a, b = (nums[51], nums[31])
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a