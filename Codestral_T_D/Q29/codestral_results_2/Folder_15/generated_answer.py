def gcf_two_nums(lst):
    a, b = lst[:2]
    while b != 0:
        a, b = (b, a % b)
    return a