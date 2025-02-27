def find_second_largest_num(lst):
    slice_lst = lst[42:69]
    if len(slice_lst) < 2:
        return None
    else:
        max_num = second_max = float('-inf')
        for num in slice_lst:
            if num > max_num:
                second_max = max_num
                max_num = num
            elif num > second_max and num < max_num:
                second_max = num
        return second_max