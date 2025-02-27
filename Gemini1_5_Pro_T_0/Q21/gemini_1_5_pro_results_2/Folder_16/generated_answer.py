def all_ints_div_by_num(lst):
    result = []
    for i in range(max(13, len(lst)), min(69, len(lst))):
        if lst[i] % 71 == 0:
            result.append(lst[i])
    return result