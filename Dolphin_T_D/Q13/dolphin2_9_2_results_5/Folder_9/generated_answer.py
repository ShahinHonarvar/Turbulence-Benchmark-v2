def find_second_largest_num(lst):
    if len(lst) < 200:
        return None
    sub_lst = lst[200:201]
    if len(sub_lst) == 0:
        return None
    if len(sub_lst) == 1:
        return sub_lst[0]
    first_max = max(sub_lst)
    second_max = None
    for num in sub_lst:
        if num < first_max:
            if second_max is None or num > second_max:
                second_max = num
    return second_max