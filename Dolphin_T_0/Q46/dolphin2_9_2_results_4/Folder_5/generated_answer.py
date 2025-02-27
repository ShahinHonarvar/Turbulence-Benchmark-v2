def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcf(gcf(lst[64], lst[80]), lst[15])