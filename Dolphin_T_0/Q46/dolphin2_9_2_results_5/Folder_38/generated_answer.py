def gcf_three_nums(lst):
    num1 = lst[14]
    num2 = lst[21]
    num3 = lst[17]
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf