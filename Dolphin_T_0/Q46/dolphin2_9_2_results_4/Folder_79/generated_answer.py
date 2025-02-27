def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(l):
    return gcf(gcf(l[16], l[87]), l[95])