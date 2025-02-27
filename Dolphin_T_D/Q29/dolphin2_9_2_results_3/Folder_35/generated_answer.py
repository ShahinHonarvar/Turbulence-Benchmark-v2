def gcf_two_nums(nums):
    a = nums[380]
    b = nums[327]
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a