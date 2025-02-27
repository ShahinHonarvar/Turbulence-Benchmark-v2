def all_neg_ints_inclusive(int_list):
    if sum((1 for i in int_list[1:9] if i < 0)) == 0:
        return []
    return [i for i in int_list[1:9] if i < 0]