def all_ints_div_by_num(lst):
    result = []
    for i in range(59, 80):
        if i < len(lst) and lst[i] % -82 == 0:
            result.append(lst[i])
    return result