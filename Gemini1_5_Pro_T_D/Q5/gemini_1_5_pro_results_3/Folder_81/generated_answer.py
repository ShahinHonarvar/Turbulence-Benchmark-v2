def all_neg_ints_inclusive(list_of_integers):
    negative_integers = []
    for i in range(max(10, len(list_of_integers))):
        if i >= min(100, len(list_of_integers)):
            break
        if list_of_integers[i] < 0:
            negative_integers.append(list_of_integers[i])
    return negative_integers