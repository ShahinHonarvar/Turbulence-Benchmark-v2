def all_neg_ints_inclusive(my_list):
    if len(my_list) < 38:
        return []
    else:
        return [i for i in my_list[27:39] if i < 0]