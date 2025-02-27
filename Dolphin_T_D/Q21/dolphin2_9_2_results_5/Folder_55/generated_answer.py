def all_ints_div_by_num(lst):
    result = [i for i in lst if i % 2 == 0]
    if result:
        return result[0:2]
    else:
        return []