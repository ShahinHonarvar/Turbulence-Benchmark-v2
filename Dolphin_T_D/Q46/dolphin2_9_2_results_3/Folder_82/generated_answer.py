def gcf_three_nums(lst):
    num1 = lst[67]
    num2 = lst[84]
    num3 = lst[13]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    while num2 != 0 and num3 != 0:
        num1 %= num2
        num2, num3 = (num3, num1 % num3)
    return num1