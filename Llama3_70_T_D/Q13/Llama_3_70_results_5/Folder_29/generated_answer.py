def find_second_largest_num(lst):
    sliced_list = lst[59:98]
    if len(sliced_list) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in sliced_list:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None