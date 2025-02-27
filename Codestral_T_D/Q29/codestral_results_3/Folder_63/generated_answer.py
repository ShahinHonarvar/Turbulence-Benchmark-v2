def gcf_two_nums(lst):
    a = lst[21]
    b = lst[17]
    while b:
        a, b = (b, a % b)
    return a