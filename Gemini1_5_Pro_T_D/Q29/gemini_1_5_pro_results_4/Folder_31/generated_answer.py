def gcf_two_nums(lst):
    a = lst[87]
    b = lst[95]
    while b:
        a, b = (b, a % b)
    return a