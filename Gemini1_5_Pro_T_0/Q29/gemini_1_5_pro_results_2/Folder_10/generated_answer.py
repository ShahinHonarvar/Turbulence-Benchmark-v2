def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[15]
    num2 = list_of_nums[99]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1