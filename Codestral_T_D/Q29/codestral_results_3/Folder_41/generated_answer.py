def gcf_two_nums(lst):
    a, b = (lst[23], lst[27])
    while b != 0:
        a, b = (b, a % b)
    return a