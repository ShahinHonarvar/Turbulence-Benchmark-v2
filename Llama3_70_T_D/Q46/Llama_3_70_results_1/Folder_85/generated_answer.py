def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[49]
    num2 = lst[46]
    num3 = lst[13]
    return gcf(gcf(num1, num2), num3)