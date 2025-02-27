def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[15:92]:
        if i % 59 != 0:
            result.append(i)
    return result