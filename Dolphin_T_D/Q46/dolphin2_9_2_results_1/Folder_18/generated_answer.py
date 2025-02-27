def gcf_three_nums(l):
    a, b, c = (l[637], l[411], l[757])

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(a, b), c)