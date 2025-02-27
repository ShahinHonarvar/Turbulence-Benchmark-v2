def gcf_two_nums(lst):
    num1 = lst[96]
    num2 = lst[32]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(num1, num2)