def gcf_two_nums(nums):
    a = nums[894]
    b = nums[801]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a