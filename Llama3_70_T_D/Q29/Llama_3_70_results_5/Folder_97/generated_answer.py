def gcf_two_nums(lst):

    def _gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return _gcf(lst[180], lst[312])