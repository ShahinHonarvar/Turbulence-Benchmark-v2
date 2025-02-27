def gcf_two_nums(lst):
    num1 = lst[19]
    num2 = lst[94]

    def gcf(a, b):
        if a % b == 0:
            return b
        else:
            return gcf(b, a % b)
    return gcf(num1, num2)