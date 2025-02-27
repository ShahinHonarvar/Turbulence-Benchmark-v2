def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[90]
    num3 = lst[27]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)