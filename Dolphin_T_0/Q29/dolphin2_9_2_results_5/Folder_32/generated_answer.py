def gcf_two_nums(nums):
    a = nums[47]
    b = nums[22]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a