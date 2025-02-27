def gcf_two_nums(lst):

    def _gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return _gcf(lst[20], lst[83])