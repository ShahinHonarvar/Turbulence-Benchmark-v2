def gcf_two_nums(lst):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return find_gcf(lst[17], lst[20])