def gcf_two_nums(lst):
    a = lst[59]
    b = lst[93]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a