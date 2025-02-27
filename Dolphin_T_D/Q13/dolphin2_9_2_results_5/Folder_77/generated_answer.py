def find_second_largest_num(lst):
    if len(lst) < 2 or not all(lst):
        return None
    max_num, second_max_num = (float('-inf'), float('-inf'))
    for num in lst[527:539]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None