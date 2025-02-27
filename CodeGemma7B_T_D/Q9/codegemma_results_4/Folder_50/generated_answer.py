def all_odd_ints_inclusive(lst):
    if not lst:
        return []
    filtered_list = [x for x in lst[70:85] if x % 2 != 0]
    return filtered_list if filtered_list else []