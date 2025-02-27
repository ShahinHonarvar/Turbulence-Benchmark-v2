def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = lst[693]
    num2 = lst[331]
    num3 = lst[668]
    gcf_12 = gcf(num1, num2)
    return gcf(gcf_12, num3)