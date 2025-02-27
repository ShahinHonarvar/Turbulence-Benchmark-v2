def gcf_two_nums(lst):
    a = lst[49]
    b = lst[31]
    while b:
        a, b = (b, a % b)
    return a