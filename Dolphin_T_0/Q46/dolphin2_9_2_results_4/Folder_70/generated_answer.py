def gcf_three_nums(lst):
    num1 = lst[990]
    num2 = lst[671]
    num3 = lst[711]
    gcf = 1
    for i in range(1, max(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf