def gcf_three_nums(lst):
    num1, num2, num3 = (lst[252], lst[149], lst[564])
    gcd = max((factor for factor in range(num1, 0, -1) if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0)))
    return gcd