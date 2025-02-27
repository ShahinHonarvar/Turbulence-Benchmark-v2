def all_neg_ints_exclusive(coords_list):
    if coords_list == []:
        return []
    neg_list = [num for num in coords_list[3:8] if num < 0]
    return neg_list