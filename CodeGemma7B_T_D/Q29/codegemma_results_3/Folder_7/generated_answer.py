def gcf_two_nums(lst):
    a = lst[224]
    b = lst[663]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a