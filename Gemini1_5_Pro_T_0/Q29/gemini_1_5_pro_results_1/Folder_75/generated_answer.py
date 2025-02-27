def gcf_two_nums(nums):
    a = nums[42]
    b = nums[25]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a