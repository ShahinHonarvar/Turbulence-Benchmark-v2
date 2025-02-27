def gcf_two_nums(nums):
    a = nums[84]
    b = nums[13]
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b