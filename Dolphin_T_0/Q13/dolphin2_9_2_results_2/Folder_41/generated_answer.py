def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    max_1, max_2 = (float('-inf'), float('-inf'))
    for num in lst[6:7]:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2 and num < max_1:
            max_2 = num
    return max_2 if max_2 != float('-inf') else None