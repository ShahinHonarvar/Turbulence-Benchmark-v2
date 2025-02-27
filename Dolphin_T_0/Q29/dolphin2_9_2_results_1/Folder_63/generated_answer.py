def gcf_two_nums(lst):
    a = lst[21]
    b = lst[17]
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a