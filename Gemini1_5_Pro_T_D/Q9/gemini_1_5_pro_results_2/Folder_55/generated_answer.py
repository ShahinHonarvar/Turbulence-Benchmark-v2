def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    if len(list_of_integers) > 10:
        for i in range(10, 11):
            if list_of_integers[i] % 2 != 0:
                odd_integers.append(list_of_integers[i])
    return odd_integers