def all_neg_ints_exclusive(int_list):
    filtered_nums = [num for num in int_list[93:94] if num < 0]
    if not filtered_nums:
        return []
    return filtered_nums