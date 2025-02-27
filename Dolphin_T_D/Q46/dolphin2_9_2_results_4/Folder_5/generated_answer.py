def gcf_three_nums(lst):
    num1 = lst[64]
    num2 = lst[80]
    num3 = lst[15]
    d = min(num1, num2, num3)
    while d > 1:
        if num1 % d == 0 and num2 % d == 0 and (num3 % d == 0):
            return d
        else:
            d -= 1
    return 1