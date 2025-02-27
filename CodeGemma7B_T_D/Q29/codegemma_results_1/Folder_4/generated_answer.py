def gcf_two_nums(lst):
    x, y = (lst[76], lst[57])
    while y:
        x, y = (y, x % y)
    return x