def all_neg_ints_inclusive(int_list):
    if len(int_list) < 80:
        return []
    else:
        return [i for i in int_list[29:80] if i < 0]