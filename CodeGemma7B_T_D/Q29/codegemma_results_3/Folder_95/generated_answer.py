def gcf_two_nums(lst):
    x, y = (lst[43], lst[99])
    while y:
        x, y = (y, x % y)
    return x