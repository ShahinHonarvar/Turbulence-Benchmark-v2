def gcf_two_nums(nums):
    a = nums[3]
    b = nums[8]
    if a == 0:
        return b
    elif b == 0:
        return a
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a