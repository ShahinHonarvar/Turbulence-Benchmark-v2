def all_odd_ints_inclusive(list_of_integers):
    odd_ints = []
    for i in range(min(2, len(list_of_integers))):
        if list_of_integers[i] % 2 != 0:
            odd_ints.append(list_of_integers[i])
    return odd_ints