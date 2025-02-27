def all_pos_ints_inclusive(integer_list):
    start = 246
    end = 750
    if start < 0 or end > len(integer_list) - 1:
        return []
    return [i for i in integer_list[start:end + 1] if i > 0]