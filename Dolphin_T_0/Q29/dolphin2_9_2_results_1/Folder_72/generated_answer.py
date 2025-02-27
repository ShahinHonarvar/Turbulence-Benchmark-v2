def gcf_two_nums(lst):
    a = (lst[17], lst[36])

    def gcf(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcf(a - b, b)
        return gcf(a, b - a)
    return gcf(*a)