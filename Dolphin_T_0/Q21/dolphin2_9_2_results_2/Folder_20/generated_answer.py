def all_ints_div_by_num(lst):
    start = 73
    end = 82
    result = []
    for i in range(start, end + 1):
        if lst[i] % -57 == 0:
            result.append(lst[i])
    return result