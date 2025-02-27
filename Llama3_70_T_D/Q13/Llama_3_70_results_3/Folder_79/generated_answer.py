def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    else:
        lst = lst[4:] + lst[:5]
        max_num = max(lst)
        second_max_num = max((i for i in lst if i != max_num))
        return second_max_num