def all_neg_ints_exclusive(int_list):
    low, high = (389, 748)
    if len(int_list) < high:
        return []
    neg_ints = [num for num in int_list[low:high] if num < 0]
    return neg_ints