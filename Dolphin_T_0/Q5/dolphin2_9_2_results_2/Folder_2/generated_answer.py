def all_neg_ints_inclusive(lst):
    specified_neg_ints = [num for num in lst[15:40] if num < 0]
    if len(specified_neg_ints) > 0:
        return specified_neg_ints
    else:
        return []