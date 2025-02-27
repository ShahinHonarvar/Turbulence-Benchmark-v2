def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[76]
    num2 = lst[35]
    num3 = lst[74]
    gcf_12 = gcf(num1, num2)
    return gcf(gcf_12, num3)