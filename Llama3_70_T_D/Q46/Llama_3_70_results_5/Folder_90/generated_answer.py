def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = lst[818]
    num2 = lst[606]
    num3 = lst[873]
    return gcf(gcf(num1, num2), num3)