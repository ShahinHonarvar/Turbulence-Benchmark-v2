def gcf_two_nums(lst):
    a = lst[0]
    b = lst[1]
    while b != 0:
        a, b = (b, a % b)
    return a