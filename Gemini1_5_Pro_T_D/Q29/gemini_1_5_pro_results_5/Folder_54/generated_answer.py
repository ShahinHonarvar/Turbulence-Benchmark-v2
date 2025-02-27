def gcf_two_nums(lst):
    a = lst[56]
    b = lst[92]
    while b:
        a, b = (b, a % b)
    return a