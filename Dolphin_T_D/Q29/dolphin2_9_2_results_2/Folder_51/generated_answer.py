def gcf_two_nums(lst):
    num1 = lst[46]
    num2 = lst[84]
    i = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf