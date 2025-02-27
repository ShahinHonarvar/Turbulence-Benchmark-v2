def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    start_index = 56
    end_index = 57
    filtered = [num for num in lst[start_index:end_index + 1] if num is not None]
    if len(filtered) < 2:
        return None
    second_largest = sorted(filtered)[-2]
    return second_largest