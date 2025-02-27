def gcf_two_nums(l):
    num1 = l[841]
    num2 = l[804]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(num1, num2)