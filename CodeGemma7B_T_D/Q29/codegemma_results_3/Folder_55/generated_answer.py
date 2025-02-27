def gcf_two_nums(nums):
    a = nums[2]
    b = nums[1]
    if a % b == 0:
        return b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a