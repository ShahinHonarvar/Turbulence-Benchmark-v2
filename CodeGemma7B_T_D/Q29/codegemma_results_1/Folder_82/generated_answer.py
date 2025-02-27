def gcf_two_nums(lst):
    num1 = lst[33]
    num2 = lst[72]
    gcd = 1
    d = 2
    while d <= num1 and d <= num2:
        if num1 % d == 0 and num2 % d == 0:
            gcd = d
        d += 1
    return gcd