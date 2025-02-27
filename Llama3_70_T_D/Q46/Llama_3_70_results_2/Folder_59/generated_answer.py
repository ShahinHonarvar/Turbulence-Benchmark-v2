def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[7]
    num2 = lst[6]
    num3 = lst[8]
    return gcf(gcf(num1, num2), num3)