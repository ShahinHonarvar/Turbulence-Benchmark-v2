def gcf_two_nums(nums):
    if len(nums) != 2:
        raise ValueError('The list should have only two elements')
    num1, num2 = nums
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1