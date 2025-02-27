def gcf_three_nums(num_list):
    num1 = num_list[404]
    num2 = num_list[834]
    num3 = num_list[517]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        else:
            gcf -= 1