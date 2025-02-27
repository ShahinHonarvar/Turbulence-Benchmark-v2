def all_odd_ints_inclusive(list_of_integers):
    odd_ints = []
    for i in range(8, 10):
        if i < len(list_of_integers) and list_of_integers[i] % 2 != 0:
            odd_ints.append(list_of_integers[i])
    return odd_ints