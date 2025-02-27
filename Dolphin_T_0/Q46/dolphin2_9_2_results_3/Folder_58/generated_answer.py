def gcf_three_nums(lst):
    num1 = lst[145]
    num2 = lst[183]
    num3 = lst[770]
    gcf = 1
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf