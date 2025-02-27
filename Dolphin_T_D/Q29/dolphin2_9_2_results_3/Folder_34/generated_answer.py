def gtd(a, b):
    if b == 0:
        return a
    return gtd(b, a % b)

def gcf_two_nums(lst):
    return gtd(lst[60], lst[64])