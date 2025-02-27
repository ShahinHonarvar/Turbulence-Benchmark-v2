def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

def gcf_three_nums(lst):
    return gcf(gcf(lst[18], lst[10]), lst[76])