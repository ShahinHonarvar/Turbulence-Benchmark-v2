def gcf_two_nums(lst):
    a = lst[894]
    b = lst[801]
    while b:
        a, b = (b, a % b)
    return a