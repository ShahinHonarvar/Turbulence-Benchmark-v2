def gcf_two_nums(lst):
    a = lst[36]
    b = lst[54]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a