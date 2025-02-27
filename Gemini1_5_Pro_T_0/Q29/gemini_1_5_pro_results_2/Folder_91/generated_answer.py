def gcf_two_nums(lst):
    a = lst[4]
    b = lst[0]
    while b:
        a, b = (b, a % b)
    return a