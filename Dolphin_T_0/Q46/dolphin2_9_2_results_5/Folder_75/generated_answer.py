def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

def gcf_three_nums(l):
    return gcf(gcf(l[70], l[98]), l[22])