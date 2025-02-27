def all_ints_not_div_by_num(lst):
    result = []
    for i in range(max(50, 0), min(len(lst), 200)):
        if lst[i] % -34 != 0:
            result.append(lst[i])
    return result