def all_ints_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if i >= 87 and i <= 89:
            if lst[i] % 55 == 0:
                result.append(lst[i])
    return result