def gcf_two_nums(nums):
    a = nums[88]
    b = nums[35]
    if a == 0 or b == 0:
        return 0
    while b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a