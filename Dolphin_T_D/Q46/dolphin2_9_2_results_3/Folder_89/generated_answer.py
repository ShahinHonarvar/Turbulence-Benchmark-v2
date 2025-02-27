def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(l):
    if len(l) < 11:
        raise ValueError('List is not long enough')
    return gcf(l[63], gcf(l[73], l[11]))