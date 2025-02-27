def gcf_two_nums(lst):
    a = lst[872]
    b = lst[219]
    while b:
        a, b = (b, a % b)
    return a