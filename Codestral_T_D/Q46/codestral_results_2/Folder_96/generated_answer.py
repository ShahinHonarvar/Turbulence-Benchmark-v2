def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[29]
    num2 = lst[74]
    num3 = lst[49]
    return gcf(gcf(num1, num2), num3)