def gcf_two_nums(lst):
    a = lst[534]
    b = lst[630]
    while b:
        a, b = (b, a % b)
    return a