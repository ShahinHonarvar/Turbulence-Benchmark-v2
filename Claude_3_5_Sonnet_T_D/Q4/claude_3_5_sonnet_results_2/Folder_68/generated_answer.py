def all_pos_ints_exclusive(integer_list):
    if len(integer_list) <= 2:
        return []
    start = 1
    end = min(8, len(integer_list) - 1)
    result = [num for num in integer_list[start:end] if num > 0]
    return result