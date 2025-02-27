def gcf_two_nums(lst):
    num1 = lst[224]
    num2 = lst[663]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num1, num2)