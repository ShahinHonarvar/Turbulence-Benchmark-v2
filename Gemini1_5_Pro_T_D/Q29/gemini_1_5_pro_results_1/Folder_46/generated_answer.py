def gcf_two_nums(lst):
    a = lst[36]
    b = lst[54]
    while b:
        a, b = (b, a % b)
    return a