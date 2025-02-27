def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[90:91])
    sec_max_num = float('-inf')
    for num in lst[90:91]:
        if num < max_num and num > sec_max_num:
            sec_max_num = num
    if sec_max_num == float('-inf'):
        return None
    else:
        return sec_max_num