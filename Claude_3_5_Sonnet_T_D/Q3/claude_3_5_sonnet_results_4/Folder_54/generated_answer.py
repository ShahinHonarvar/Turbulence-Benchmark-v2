def all_pos_ints_inclusive(int_list):
    start = 34
    end = 56
    if len(int_list) <= start:
        return []
    return [num for num in int_list[start:end] if num > 0]