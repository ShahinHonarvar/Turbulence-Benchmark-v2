def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(lst):
    return gcf(gcf(lst[14], lst[21]), lst[17])