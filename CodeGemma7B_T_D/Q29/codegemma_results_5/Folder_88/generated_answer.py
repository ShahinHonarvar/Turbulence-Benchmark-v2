def gcf_two_nums(list_of_int):
    a = list_of_int[27]
    b = list_of_int[34]
    if a == b:
        return a
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    while greater % smaller != 0:
        temp = greater % smaller
        greater = smaller
        smaller = temp
    return smaller