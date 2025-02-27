def all_ints_not_div_by_num(lst):
    if -3 not in [lst[i] % -3 for i in range(len(lst)) if 0 <= i < 8]:
        return []
    return [val for val in lst if 0 <= lst.index(val) < 8 and val % -3 != 0]