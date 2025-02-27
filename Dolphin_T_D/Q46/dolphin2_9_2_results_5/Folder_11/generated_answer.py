def gcf(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcf(a - b, b)
    return gcf(a, b - a)

def gcf_three_nums(l):
    return gcf(gcf(l[37], l[30]), l[48])