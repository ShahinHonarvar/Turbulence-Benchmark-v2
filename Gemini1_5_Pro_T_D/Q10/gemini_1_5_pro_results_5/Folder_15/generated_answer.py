def all_odd_ints_exclusive(list_of_integers):
    odd_integers = []
    for i in range(1, 3):
        if list_of_integers[i] % 2 != 0:
            odd_integers.append(list_of_integers[i])
    return odd_integers