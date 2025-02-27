def all_neg_ints_inclusive(a):
    if sum((int(x) < 0 for x in a[262:747])) == 0:
        return []
    return [int(x) for x in a[262:747] if int(x) < 0]