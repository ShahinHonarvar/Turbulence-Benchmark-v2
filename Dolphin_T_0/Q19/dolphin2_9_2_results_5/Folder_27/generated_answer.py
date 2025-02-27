def all_ints_not_div_by_num(lst):
    result = []
    for i in range(14, 21):
        if i < len(lst):
            if lst[i] % -93 != 0:
                result.append(lst[i])
    return result