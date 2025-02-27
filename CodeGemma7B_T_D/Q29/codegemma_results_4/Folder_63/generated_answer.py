def gcf_two_nums(lst):
    a, b = (lst[21], lst[17])
    while b:
        a, b = (b, a % b)
    return a