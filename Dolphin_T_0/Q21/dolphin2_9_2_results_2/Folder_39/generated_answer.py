def all_ints_div_by_num(lst):
    desired_num = -12
    result = [x for i, x in enumerate(lst[9:53]) if x % desired_num == 0]
    return result if len(result) > 0 else []