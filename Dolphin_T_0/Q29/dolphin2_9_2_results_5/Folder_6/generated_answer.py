def gcf_two_nums(lst):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    if len(lst) < 80:
        return 'Error: List not long enough'
    return gcf(lst[25], lst[80])