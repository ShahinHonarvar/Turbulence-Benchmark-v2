def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[16]
    num2 = lst[87]
    num3 = lst[95]
    return gcf(gcf(num1, num2), num3)