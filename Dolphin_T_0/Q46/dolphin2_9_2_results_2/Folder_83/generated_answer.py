def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[54]
    num3 = lst[13]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    result = gcf(min(num1, num2, num3), gcf(num1, num2, num3))
    return result