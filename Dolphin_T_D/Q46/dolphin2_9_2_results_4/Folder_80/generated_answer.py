def gcf_three_nums(lst):
    num1 = lst[13]
    num2 = lst[76]
    num3 = lst[44]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    gcf_val = gcf(num1, num2)
    gcf_val = gcf(gcf_val, num3)
    return gcf_val