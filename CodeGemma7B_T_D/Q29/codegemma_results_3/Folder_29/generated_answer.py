def gcf_two_nums(num_list):
    num1 = num_list[96]
    num2 = num_list[57]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i