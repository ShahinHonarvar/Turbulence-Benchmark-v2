def all_neg_ints_inclusive(lst):
    neg_integers = [i for i in lst[661:925] if i < 0]
    return neg_integers if len(neg_integers) > 0 else []