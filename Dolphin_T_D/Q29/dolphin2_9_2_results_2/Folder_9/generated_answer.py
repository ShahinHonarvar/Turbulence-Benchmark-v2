def gcf_two_nums(lst):
    num1 = lst[84]
    num2 = lst[63]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num1, num2)