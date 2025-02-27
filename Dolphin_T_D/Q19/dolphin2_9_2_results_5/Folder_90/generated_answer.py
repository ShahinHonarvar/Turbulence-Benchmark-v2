def all_ints_not_div_by_num(lst):
    result = []
    for i in range(767, 905):
        if i % -430 != 0:
            result.append(lst[i])
    return result