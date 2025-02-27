def gcf_two_nums(lst):
    a = lst[372]
    b = lst[752]
    while b:
        a, b = (b, a % b)
    return a