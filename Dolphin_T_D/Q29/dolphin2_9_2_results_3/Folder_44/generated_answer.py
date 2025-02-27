def gcf_two_nums(lst):
    num1 = lst[56]
    num2 = lst[88]
    i = 1
    while i <= num1:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf