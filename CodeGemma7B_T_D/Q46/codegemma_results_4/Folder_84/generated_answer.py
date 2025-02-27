def gcf_three_nums(nums):
    num1, num2, num3 = (nums[695], nums[710], nums[914])
    return greatest_common_factor(num1, greatest_common_factor(num2, num3))

def greatest_common_factor(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1