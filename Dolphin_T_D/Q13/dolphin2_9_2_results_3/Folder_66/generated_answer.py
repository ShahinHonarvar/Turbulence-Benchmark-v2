def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    sub_lst = lst[50:55]
    if len(set(sub_lst)) < 2:
        return None
    max_num = max(sub_lst)
    second_max_num = None
    for num in sub_lst:
        if num < max_num and (second_max_num is None or second_max_num < num):
            second_max_num = num
    return second_max_num