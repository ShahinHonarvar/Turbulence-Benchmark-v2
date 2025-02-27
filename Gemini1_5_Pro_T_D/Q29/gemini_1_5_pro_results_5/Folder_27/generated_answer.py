def gcf_two_nums(nums):
    a = nums[15]
    b = nums[40]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b