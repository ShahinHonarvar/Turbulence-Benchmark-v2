def gcf_two_nums(lst):
    a = lst[36]
    b = lst[85]
    if a > b:
        a, b = (b, a)
    while a:
        a, b = (b % a, a)
    return a