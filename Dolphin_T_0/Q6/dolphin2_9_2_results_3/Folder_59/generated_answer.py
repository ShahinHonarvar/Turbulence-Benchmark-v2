def all_neg_ints_exclusive(list_of_integers):
    neg_ints = [num for num in list_of_integers[1:-1] if num < 0]
    return neg_ints