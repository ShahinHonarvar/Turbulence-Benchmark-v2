def all_ints_div_by_num(lst):
    result = []
    for i in range(max(0, 29), min(len(lst), 52)):
        if lst[i] % -37 == 0:
            result.append(lst[i])
    return result