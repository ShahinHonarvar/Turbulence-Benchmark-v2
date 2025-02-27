def gcf_two_nums(nums):
    if len(nums) != 998:
        raise ValueError('List must have 998 elements')
    a, b = (nums[534], nums[630])
    while b:
        a, b = (b, a % b)
    return a