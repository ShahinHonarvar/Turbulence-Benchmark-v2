def all_neg_ints_exclusive(lst):
    neg_integers = [neg for i, neg in enumerate(lst[50:200]) if neg < 0]
    if not neg_integers:
        return []
    return neg_integers