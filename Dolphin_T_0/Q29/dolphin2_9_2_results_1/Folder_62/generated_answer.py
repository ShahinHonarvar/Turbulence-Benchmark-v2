def gcf_two_nums(lst):
    a, b = (lst[51], lst[31])
    while b:
        a, b = (b, a % b)
    return a