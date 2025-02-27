def gcf_two_nums(lst):
    a = lst[224]
    b = lst[663]
    while b:
        a, b = (b, a % b)
    return a