def gcf_two_nums(nums):
    if len(nums) < 9:
        raise ValueError('Input list must have at least 9 elements')
    num1 = nums[3]
    num2 = nums[8]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1