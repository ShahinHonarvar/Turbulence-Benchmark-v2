def gcf_three_nums(lst):
    gcf = lambda a, b: a if b == 0 else gcf(b, a % b)
    return gcf(gcf(lst[78], lst[19]), lst[13])