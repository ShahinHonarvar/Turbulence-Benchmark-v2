def find_second_largest_num(lst):
    if not lst:
        return None
    max_val = float('-inf')
    second_max_val = float('-inf')
    for num in lst[68:87]:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num != max_val and num > second_max_val:
            second_max_val = num
    return second_max_val if second_max_val != float('-inf') else None