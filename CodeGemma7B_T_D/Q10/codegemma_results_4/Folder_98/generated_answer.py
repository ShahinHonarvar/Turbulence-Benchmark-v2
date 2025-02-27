def all_odd_ints_exclusive(list_of_integers):
    odd_list = []
    for i in range(0, 7):
        if i % 2 != 0 and i < 7 and (i >= 0):
            odd_list.append(list_of_integers[i])
    return odd_list