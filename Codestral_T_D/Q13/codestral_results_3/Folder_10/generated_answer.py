def find_second_largest_num(lst):
    sublist = lst[25:60]
    if len(sublist) < 2:
        return None
    else:
        max_num = second_max_num = float('-inf')
        for num in sublist:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif second_max_num < num < max_num:
                second_max_num = num
        return second_max_num if second_max_num != float('-inf') else None