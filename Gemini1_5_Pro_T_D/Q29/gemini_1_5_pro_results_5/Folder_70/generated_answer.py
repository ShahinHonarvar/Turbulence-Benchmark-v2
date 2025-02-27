def gcf_two_nums(lst):
    a = lst[300]
    b = lst[616]
    while b:
        a, b = (b, a % b)
    return a