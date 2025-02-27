def gcf_three_nums(lst):
    num1 = lst[78]
    num2 = lst[19]
    num3 = lst[13]
    gcf = 1
    i = 1
    while i <= min(num1, num2, num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf