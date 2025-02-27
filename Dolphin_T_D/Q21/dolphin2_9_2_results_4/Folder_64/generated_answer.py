def all_ints_div_by_num(lst):
    result = []
    for i in lst[0:1]:
        if i % 4 == 0:
            result.append(i)
    return result