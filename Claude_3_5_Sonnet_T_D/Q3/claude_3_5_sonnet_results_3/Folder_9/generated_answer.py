def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 71:
        return []
    start = max(70, 0)
    end = min(201, len(integer_list))
    return [num for num in integer_list[start:end] if num > 0]