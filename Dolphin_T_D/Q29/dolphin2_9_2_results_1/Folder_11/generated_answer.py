def gcf_two_nums(lst):
    num1 = lst[64]
    num2 = lst[80]
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    i = 1
    while i <= smaller:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf