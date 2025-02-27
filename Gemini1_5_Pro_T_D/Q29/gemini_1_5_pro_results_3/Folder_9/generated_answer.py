def gcf_two_nums(lst):
    a = lst[84]
    b = lst[63]
    while b:
        a, b = (b, a % b)
    return a