def gcf_two_nums(lst):
    a = lst[198]
    b = lst[212]
    while b:
        a, b = (b, a % b)
    return a