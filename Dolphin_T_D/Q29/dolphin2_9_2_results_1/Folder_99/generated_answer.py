def gcf_two_nums(my_list):
    num1 = my_list[279]
    num2 = my_list[812]
    gcf = min(num1, num2)
    while num1 % gcf != 0 or num2 % gcf != 0:
        gcf -= 1
    return gcf