def gcf_two_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[83]
    num2 = lst[14]
    return gcf(num1, num2)