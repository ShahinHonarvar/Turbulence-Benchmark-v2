def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    for i in range(75, 95):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % 2 != 0:
                odd_integers.append(list_of_integers[i])
    return odd_integers