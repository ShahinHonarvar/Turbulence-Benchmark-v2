def all_neg_ints_exclusive(int_list):
    if len(int_list) < 53 or not int_list[27:53]:
        return []
    else:
        return [i for i in int_list[27:53] if i < 0]