def all_neg_ints_inclusive(lst):
    neg_ints = [i for i in lst[209:557] if i < 0]
    if not neg_ints:
        return []
    else:
        return neg_ints