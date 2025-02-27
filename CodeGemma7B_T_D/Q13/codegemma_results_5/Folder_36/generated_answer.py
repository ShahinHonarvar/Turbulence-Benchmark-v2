def find_second_largest_num(lst):
    if not lst or len(lst) < 2:
        return None
    max_num = lst[0]
    second_max_num = float('-inf')
    for num in lst[246:751]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num:
            second_max_num = num
    return second_max_num or None