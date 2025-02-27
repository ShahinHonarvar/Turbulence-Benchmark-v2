def gcf_two_nums(l):
    a = l[43]
    b = l[99]
    if a == 0:
        return b

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(a, b)