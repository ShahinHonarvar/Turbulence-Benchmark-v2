def all_neg_ints_exclusive(int_list):
    start, end = (111, 473)
    if start < 0 or end > len(int_list):
        return []
    return [num for num in int_list[start:end] if num < 0]