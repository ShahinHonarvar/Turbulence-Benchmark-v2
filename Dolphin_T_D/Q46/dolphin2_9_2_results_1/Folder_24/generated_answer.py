def gcf_three_nums(lst):
    num1 = lst[18]
    num2 = lst[37]
    num3 = lst[43]
    i = 1
    while i > 0:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcd = i
        else:
            i -= 1
    return gcd