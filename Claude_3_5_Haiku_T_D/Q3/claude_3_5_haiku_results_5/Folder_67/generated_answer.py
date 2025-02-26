def all_pos_ints_inclusive(lst):
    if len(lst) <= 22:
        return []
    end_index = min(50, len(lst) - 1)
    result = [num for num in lst[22:end_index + 1] if num > 0]
    return result