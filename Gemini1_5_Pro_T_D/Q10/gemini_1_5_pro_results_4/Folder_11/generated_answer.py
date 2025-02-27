def all_odd_ints_exclusive(list_of_integers):
    odd_integers = []
    for i in range(16, 99):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 2 != 0:
            odd_integers.append(list_of_integers[i])
    return odd_integers