def gcf_two_nums(lst):
    a = lst[36]
    b = lst[85]
    while b:
        a, b = (b, a % b)
    return a