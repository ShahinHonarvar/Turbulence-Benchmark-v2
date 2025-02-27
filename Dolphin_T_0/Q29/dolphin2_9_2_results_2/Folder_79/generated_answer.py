def gcf_two_nums(numbers_list):
    num1 = numbers_list[85]
    num2 = numbers_list[51]
    gcf = min(num1, num2)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0:
            return gcf
        gcf -= 1
    return 1