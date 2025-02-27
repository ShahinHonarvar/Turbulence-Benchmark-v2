def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    max_val = max(lst[33:37])
    sec_max = None
    for val in lst[33:37]:
        if val != max_val:
            if sec_max is None or val > sec_max:
                sec_max = val
    return sec_max