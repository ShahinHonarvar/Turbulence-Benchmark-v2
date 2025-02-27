def gcf_two_nums(nums):
    a = nums[36]
    b = nums[54]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a