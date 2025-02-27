def gcf_three_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    num1 = lst[25]
    num2 = lst[76]
    num3 = lst[57]
    return gcf(gcf(num1, num2), num3)