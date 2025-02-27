def gcf_two_nums(lst):
    if lst[90] == 0 or lst[84] == 0:
        return 0
    a, b = (lst[90], lst[84])
    while b != 0:
        a, b = (b, a % b)
    return abs(a)