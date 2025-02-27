def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(lst):
    return gcf(gcf(lst[38], lst[52]), lst[69])