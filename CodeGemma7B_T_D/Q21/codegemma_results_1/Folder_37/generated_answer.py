def all_ints_div_by_num(lst):
    result = []
    for i in lst[4:5]:
        if i % 3 == 0:
            result.append(i)
    return result