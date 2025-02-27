def all_ints_div_by_num(lst):
    result = []
    for i in range(max(23, 0), min(len(lst), 66)):
        if lst[i] % -46 == 0:
            result.append(lst[i])
    return result