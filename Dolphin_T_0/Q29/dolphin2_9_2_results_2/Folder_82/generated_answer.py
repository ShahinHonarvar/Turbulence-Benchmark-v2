def gcf_two_nums(lst):
    num1 = lst[33]
    num2 = lst[72]
    gcf = 1
    i = 2
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf