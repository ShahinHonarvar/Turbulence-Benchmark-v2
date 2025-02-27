def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1 = lst[15]
    num2 = lst[51]
    num3 = lst[76]
    return gcf(gcf(num1, num2), num3)