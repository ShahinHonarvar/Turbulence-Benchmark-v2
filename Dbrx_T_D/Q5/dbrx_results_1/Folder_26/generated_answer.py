def all_neg_ints_inclusive(int_list):
    if len(int_list) >= 100:
        return [i for i in int_list[62:100] if i < 0]
    else:
        return []