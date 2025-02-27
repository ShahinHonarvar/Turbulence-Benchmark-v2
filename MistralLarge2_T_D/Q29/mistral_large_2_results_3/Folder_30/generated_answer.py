def gcf_two_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) > 85:
        return gcf(lst[85], lst[33])
    else:
        return None