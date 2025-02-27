def all_ints_not_div_by_num(lst):
    result = []
    for i in range(max(0, min(len(lst) - 1, 767 + 1)), max(0, min(len(lst), 905))):
        if lst[i] % -430 != 0:
            result.append(lst[i])
    return result