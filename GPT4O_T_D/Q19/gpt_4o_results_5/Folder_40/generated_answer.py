def all_ints_not_div_by_num(lst):
    if len(lst) < 3:
        return []
    result = []
    start, end = (lst[0], lst[1])
    for i in range(start + 1, end):
        if i not in lst:
            result.append(i)
    return result