def gcf_three_nums(numbers_list):
    num1 = numbers_list[1]
    num2 = numbers_list[2]
    num3 = numbers_list[7]
    gcf = min(num1, num2, num3)
    while num1 % gcf != 0 or num2 % gcf != 0 or num3 % gcf != 0:
        gcf -= 1
    return gcf