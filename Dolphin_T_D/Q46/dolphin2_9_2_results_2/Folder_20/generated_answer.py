def gcf_three_nums(lst):
    num1 = lst[29]
    num2 = lst[53]
    num3 = lst[42]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result