def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(lst) > 51:
        num1 = lst[21]
        num2 = lst[51]
        num3 = lst[33]
        num4 = gcf(num1, num2)
        return gcf(num4, num3)