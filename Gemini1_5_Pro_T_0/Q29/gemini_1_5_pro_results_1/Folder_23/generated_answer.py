def gcf_two_nums(lst):
    a = lst[48]
    b = lst[74]
    while b:
        a, b = (b, a % b)
    return a