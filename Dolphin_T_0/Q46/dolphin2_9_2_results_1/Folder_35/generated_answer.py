def gcf_three_nums(lst):
    num1 = lst[742]
    num2 = lst[888]
    num3 = lst[629]

    def gcf(a, b):
        if a == 0:
            return b
        else:
            return gcf(b % a, a)
    result = gcf(gcf(num1, num2), num3)
    return result