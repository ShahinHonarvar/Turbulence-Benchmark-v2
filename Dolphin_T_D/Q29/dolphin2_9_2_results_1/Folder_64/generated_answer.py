def gcf_two_nums(num_list):
    num1 = num_list[6]
    num2 = num_list[9]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return num1