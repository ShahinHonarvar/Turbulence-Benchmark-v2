def all_neg_ints_inclusive(int_list):
    if len(int_list) < 80:
        return []
    result = [i for i in int_list[40:81] if i < 0]
    return result