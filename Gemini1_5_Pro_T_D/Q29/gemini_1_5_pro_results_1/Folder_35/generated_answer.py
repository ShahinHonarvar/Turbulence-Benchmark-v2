def gcf_two_nums(lst):
    a = lst[380]
    b = lst[327]
    while b:
        a, b = (b, a % b)
    return a