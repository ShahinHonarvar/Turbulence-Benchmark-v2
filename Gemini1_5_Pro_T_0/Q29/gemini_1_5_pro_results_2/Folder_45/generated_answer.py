def gcf_two_nums(lst):
    a = lst[47]
    b = lst[97]
    while b:
        a, b = (b, a % b)
    return a