def gcf_two_nums(l):
    num1 = l[360]
    num2 = l[722]

    def gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    return gcf(num1, num2)