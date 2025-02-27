def gcf_three_nums(lst):
    num1 = lst[145]
    num2 = lst[183]
    num3 = lst[770]
    i = 1
    while i <= num1 and i <= num2 and (i <= num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf