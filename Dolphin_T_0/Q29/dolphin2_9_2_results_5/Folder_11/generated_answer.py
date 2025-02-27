def gcf_two_nums(nums):
    number1 = nums[64]
    number2 = nums[80]
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1
    return number1