def all_neg_ints_inclusive(lst):
    negative_integers = [num for num in lst[:9] if num < 0]
    return negative_integers if len(negative_integers) else []