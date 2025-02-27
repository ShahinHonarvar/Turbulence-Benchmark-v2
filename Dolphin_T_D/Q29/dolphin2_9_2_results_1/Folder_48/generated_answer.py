def gcf_two_nums(lst):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    if 618 < len(lst) and 195 < len(lst):
        return gcf(lst[618], lst[195])
    raise Exception('Invalid list')