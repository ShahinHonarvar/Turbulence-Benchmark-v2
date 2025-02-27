def gcf_two_nums(nums):
    a = nums[20]
    b = nums[83]
    while b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a