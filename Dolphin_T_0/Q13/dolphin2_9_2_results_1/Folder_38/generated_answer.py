def find_second_largest_num(lst):
    if 63 >= len(lst) >= 22:
        slice_lst = lst[22:64]
        if len(set(slice_lst)) < 2:
            return None
        elif len(set(slice_lst)) == 2:
            return min(set(slice_lst))
        else:
            first_max_num = max(set(slice_lst))
            second_max_num = max([num for num in set(slice_lst) if num < first_max_num])
            return second_max_num
    else:
        return None