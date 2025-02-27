def all_neg_ints_inclusive(int_list):
    if len(int_list) < 201:
        return []
    else:
        return [i for i in int_list[100:201] if i < 0]