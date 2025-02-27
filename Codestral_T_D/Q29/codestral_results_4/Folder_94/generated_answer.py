def gcf_two_nums(lst):
    a = lst[91]
    b = lst[45]
    while b != 0:
        a, b = (b, a % b)
    return a