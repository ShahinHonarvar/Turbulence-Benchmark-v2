def gcf_two_nums(lst):
    a = lst[66]
    b = lst[90]
    if a < b:
        a, b = (b, a)
    while b:
        a, b = (b, a % b)
    return a