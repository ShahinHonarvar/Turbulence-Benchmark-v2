def all_ints_div_by_num(lst):
    result = []
    for i in range(max(17, 0), min(64, len(lst))):
        if lst[i] % 89 == 0:
            result.append(lst[i])
    return result