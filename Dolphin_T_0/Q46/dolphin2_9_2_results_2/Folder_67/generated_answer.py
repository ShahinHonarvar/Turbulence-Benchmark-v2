def gcf_three_nums(lst):
    num1 = lst[70]
    num2 = lst[41]
    num3 = lst[20]
    i = 1
    while i <= num1 and i <= num2 and (i <= num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf