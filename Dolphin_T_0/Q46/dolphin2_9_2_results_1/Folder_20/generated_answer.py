def gcf_three_nums(lst):
    num1 = lst[29]
    num2 = lst[53]
    num3 = lst[42]
    if num1 > num2:
        if num1 > num3:
            if num2 > num3:
                greater = num1
            else:
                greater = num3
        else:
            greater = num3
    elif num2 > num3:
        if num1 > num3:
            greater = num2
        else:
            greater = num3
    else:
        greater = num2
    for i in range(greater, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
            break
    return gcf