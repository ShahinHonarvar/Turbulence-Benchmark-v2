def gcf_three_nums(lst):
    num1 = lst[22]
    num2 = lst[97]
    num3 = lst[64]
    gcf = 1
    for i in range(1, max(num1, num2, num3) + 1):
        if i % num1 == 0 and i % num2 == 0 and (i % num3 == 0):
            gcf = i
    return gcf