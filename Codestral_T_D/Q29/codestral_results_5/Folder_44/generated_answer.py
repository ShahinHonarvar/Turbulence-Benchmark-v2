def gcf_two_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = lst[56]
    num2 = lst[88]
    return gcf(num1, num2)