def gcf_two_nums(lst):
    a = lst[86]
    b = lst[89]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(a, b)