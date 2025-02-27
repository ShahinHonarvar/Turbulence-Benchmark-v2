def find_second_largest_num(lst):
    if len(lst) <= 23:
        return None
    sliced_lst = lst[23:]
    largest = max(sliced_lst)
    sliced_lst = [num for num in sliced_lst if num != largest]
    if sliced_lst:
        return max(sliced_lst)
    else:
        return None