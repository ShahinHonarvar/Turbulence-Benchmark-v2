def gcf_two_nums(arg_list):
    num1 = arg_list[28]
    num2 = arg_list[49]
    common_factor = None
    while True:
        if num1 == num2:
            common_factor = num1
            break
        elif num1 > num2:
            num1 -= num2
        elif num2 > num1:
            num2 -= num1
    return common_factor