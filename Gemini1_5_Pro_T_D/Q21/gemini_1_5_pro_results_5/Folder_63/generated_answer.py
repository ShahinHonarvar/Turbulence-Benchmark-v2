def all_ints_div_by_num(lst):
    result = []
    for i in range(max(50, 0), min(len(lst), 55)):
        if lst[i] % 84 == 0:
            result.append(lst[i])
    return result