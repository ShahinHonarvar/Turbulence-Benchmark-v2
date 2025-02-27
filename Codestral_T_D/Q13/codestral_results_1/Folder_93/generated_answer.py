def find_second_largest_num(lst):
    sub_lst = lst[75:95]
    if len(sub_lst) < 2:
        return None
    else:
        max_num = second_max_num = float('-inf')
        for num in sub_lst:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif second_max_num < num < max_num:
                second_max_num = num
        return second_max_num if second_max_num != float('-inf') else None