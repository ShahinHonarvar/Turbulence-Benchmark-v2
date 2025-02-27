def gcf_two_nums(lst):
    num1 = lst[96]
    num2 = lst[32]
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf