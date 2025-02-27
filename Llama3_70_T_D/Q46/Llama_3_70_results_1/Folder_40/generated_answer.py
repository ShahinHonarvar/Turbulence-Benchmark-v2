def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[1]
    b = lst[6]
    c = lst[8]
    return gcf(a, gcf(b, c))