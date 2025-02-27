def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    for i in range(max(639, 0), min(len(list_of_integers), 976)):
        if list_of_integers[i] % 2 != 0:
            odd_integers.append(list_of_integers[i])
    return odd_integers