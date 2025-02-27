def gcf_two_nums(lst):
    a = lst[51]
    b = lst[27]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a