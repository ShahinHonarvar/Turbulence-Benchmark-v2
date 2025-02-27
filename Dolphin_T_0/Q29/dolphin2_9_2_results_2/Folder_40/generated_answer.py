def gcf_two_nums(lst):
    a = lst[7]
    b = lst[9]
    while b != 0:
        a, b = (b, a % b)
    return a