def all_pos_ints_inclusive(lst):
    if len(lst) <= 50:
        return []
    end_index = min(200, len(lst) - 1)
    positive_ints = [num for num in lst[50:end_index + 1] if num > 0]
    return positive_ints