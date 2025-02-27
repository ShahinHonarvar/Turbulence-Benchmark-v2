def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[22]
    num2 = lst[97]
    num3 = lst[64]
    return gcf(gcf(num1, num2), num3)