def gcf_two_nums(lst):
    x = lst[56]
    y = lst[54]
    return gcf(x, y)

def gcf(x, y):
    if y != 0:
        return gcf(y, x % y)
    else:
        return x