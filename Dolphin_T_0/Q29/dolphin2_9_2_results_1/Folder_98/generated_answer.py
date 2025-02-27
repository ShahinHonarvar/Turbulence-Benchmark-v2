def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[0]
    num2 = list_of_nums[9]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1