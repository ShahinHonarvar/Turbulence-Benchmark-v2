def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[42]
    num2 = list_of_nums[25]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num2