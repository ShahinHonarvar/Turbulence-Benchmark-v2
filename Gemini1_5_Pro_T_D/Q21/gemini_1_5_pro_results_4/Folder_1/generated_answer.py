def all_ints_div_by_num(l):
    result = []
    for i in range(max(0, 59), min(len(l), 78)):
        if l[i] % -95 == 0:
            result.append(l[i])
    return result