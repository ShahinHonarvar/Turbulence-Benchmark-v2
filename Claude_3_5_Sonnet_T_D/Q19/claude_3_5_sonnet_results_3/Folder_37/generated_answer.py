def all_ints_not_div_by_num(integers):
    result = []
    for i in range(2, len(integers) - 1):
        if integers[i] % 5 != 0:
            result.append(integers[i])
    return result