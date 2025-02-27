def gcf_three_nums(l):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(l[20], l[51]), l[62])