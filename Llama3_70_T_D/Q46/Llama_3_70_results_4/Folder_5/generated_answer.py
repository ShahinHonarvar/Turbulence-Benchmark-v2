def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[64]
    num2 = lst[80]
    num3 = lst[15]
    gcf_1_2 = gcf(num1, num2)
    return gcf(gcf_1_2, num3)