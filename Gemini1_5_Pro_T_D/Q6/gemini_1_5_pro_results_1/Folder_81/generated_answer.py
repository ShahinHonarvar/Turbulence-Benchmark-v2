def all_neg_ints_exclusive(list_of_integers):
    negative_integers = []
    for i in range(max(10, len(list_of_integers))):
        if i >= 10 and i < min(100, len(list_of_integers)) and (list_of_integers[i] < 0):
            negative_integers.append(list_of_integers[i])
    return negative_integers