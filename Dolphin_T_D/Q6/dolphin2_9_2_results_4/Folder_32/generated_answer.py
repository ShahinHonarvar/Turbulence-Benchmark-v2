def all_neg_ints_exclusive(list_of_integers):
    negatives = [num for num in list_of_integers[12:75] if num < 0]
    if not negatives:
        return []
    else:
        return negatives