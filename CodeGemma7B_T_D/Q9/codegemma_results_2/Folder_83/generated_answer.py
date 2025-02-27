def all_odd_ints_inclusive(seq):
    if len(seq) <= 200 or len(seq) <= 90:
        return []
    else:
        return seq[90:200 + 1:2]