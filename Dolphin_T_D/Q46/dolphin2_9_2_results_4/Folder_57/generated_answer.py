def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[41]
    num3 = lst[95]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)