def gcf_two_nums(lst):
    a = lst[279]
    b = lst[812]
    while b:
        a, b = (b, a % b)
    return a