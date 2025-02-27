def gcf_two_nums(lst):

    def find_gcf(a, b):
        if b == 0:
            return a
        return find_gcf(b, a % b)
    return find_gcf(lst[78], lst[93])