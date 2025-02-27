def all_ints_div_by_num(lst):
    result = []
    for i in range(min(20, len(lst)), max(20, len(lst))):
        if i < len(lst) and lst[i] % 2 == 0:
            result.append(lst[i])
    return result