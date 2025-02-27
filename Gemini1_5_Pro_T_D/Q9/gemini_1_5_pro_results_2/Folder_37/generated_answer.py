def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    for i in range(1, 6):
        if i % 2 != 0 and i in list_of_integers:
            odd_integers.append(i)
    return odd_integers