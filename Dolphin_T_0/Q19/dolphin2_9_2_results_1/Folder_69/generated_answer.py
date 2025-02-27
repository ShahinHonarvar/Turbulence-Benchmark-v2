def all_ints_not_div_by_num(lst):
    result = []
    for i in range(45, 72):
        if i % 93 != 0:
            result.append(lst[i])
    return result