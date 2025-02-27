def all_odd_ints_exclusive(list_integers):
    odd_integers = [n for i, n in enumerate(list_integers) if i not in [36, 85] and n % 2 != 0]
    return odd_integers