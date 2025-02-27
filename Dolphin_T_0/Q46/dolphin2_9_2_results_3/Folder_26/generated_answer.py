def gcf_three_nums(lst):
    num1 = lst[15]
    num2 = lst[51]
    num3 = lst[76]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result