def all_ints_div_by_num(lst):
    result = []
    for i in range(max(0, min(len(lst) - 1, 40)), min(len(lst), 69)):
        if lst[i] % 16 == 0:
            result.append(lst[i])
    return result