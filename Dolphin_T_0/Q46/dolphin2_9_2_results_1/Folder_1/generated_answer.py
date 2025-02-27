def gcf_three_nums(lst):
    num1 = lst[74]
    num2 = lst[51]
    num3 = lst[27]
    if num1 > num2:
        if num1 > num3:
            smaller = num2 if num2 < num3 else num3
        else:
            smaller = num1 if num1 < num3 else num3
    elif num2 > num3:
        smaller = num1 if num1 < num3 else num3
    else:
        smaller = num1 if num1 < num2 else num2
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
    return 1