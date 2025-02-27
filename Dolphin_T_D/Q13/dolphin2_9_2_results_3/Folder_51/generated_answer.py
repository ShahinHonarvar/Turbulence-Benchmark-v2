def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    lst = lst[1:9]
    max_val = max(lst)
    sec_max = float('-inf')
    for num in lst:
        if num != max_val and num > sec_max:
            sec_max = num
    if sec_max == float('-inf'):
        return None
    return sec_max