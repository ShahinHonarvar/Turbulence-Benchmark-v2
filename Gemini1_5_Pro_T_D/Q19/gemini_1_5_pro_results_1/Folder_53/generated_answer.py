def all_ints_not_div_by_num(lst):
    result = []
    for i in range(199, 201):
        if i >= len(lst):
            break
        if lst[i] % -200 != 0:
            result.append(lst[i])
    return result