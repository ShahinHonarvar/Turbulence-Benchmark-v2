def gcf_two_nums(nums):
    a = nums[8]
    b = nums[3]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a