def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    if len(list_of_integers) > 4:
        if list_of_integers[4] % 2 != 0:
            odd_integers.append(list_of_integers[4])
    return odd_integers