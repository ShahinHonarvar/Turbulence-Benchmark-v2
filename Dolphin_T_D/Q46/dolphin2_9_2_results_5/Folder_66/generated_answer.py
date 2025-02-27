def gcf(a, b):
    while b != 0:
        a %= b
        a, b = (b, a)
    return a

def gcf_three_nums(lst):
    a = lst[92]
    b = lst[69]
    c = lst[95]
    return gcf(gcf(a, b), c)