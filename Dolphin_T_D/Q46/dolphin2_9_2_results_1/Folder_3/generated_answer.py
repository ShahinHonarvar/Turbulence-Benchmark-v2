def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(lst):
    return gcf(gcf(lst[31], lst[69]), lst[40])