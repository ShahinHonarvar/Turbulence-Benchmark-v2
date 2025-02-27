def find_second_largest_num(lst):
    sub_lst = lst[62:100]
    if len(sub_lst) < 2:
        return None
    max_num = max(sub_lst)
    second_max_num = None
    for num in sub_lst:
        if num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num