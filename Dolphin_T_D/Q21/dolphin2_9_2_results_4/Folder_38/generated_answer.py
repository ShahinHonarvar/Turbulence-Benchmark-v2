def all_ints_div_by_num(lst):
    result = []
    for i in lst[12:16]:
        if i % -80 == 0:
            result.append(i)
    return result