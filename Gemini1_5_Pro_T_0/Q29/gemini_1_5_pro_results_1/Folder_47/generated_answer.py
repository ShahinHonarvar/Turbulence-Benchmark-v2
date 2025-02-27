def gcf_two_nums(l):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(l[28], l[17])