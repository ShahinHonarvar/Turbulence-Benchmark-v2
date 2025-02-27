def gcf_three_nums(lst):
    a, b, c = (lst[41], lst[69], lst[28])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a