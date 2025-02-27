def find_second_largest_num(lst):
    subset = lst[68:87]
    if len(subset) < 2:
        return None
    max_val = float('-inf')
    second_max_val = float('-inf')
    for num in subset:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val and num != max_val:
            second_max_val = num
    return second_max_val if second_max_val != float('-inf') else None