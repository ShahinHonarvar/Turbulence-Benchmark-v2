def gcf_two_nums(numbers_list):
    num1 = numbers_list[96]
    num2 = numbers_list[57]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1