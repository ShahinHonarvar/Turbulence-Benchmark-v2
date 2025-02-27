def gcf_two_nums(lst):
    a = lst[3]
    b = lst[8]
    while b:
        a, b = (b, a % b)
    return a