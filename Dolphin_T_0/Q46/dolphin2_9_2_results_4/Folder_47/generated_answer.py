def gcf_three_nums(lst):
    num1 = lst[36]
    num2 = lst[85]
    num3 = lst[83]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)