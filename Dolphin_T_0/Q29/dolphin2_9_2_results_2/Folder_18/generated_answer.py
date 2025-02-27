def gcf_two_nums(lst):
    num1 = lst[872]
    num2 = lst[219]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1