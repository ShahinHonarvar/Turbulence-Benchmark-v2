def all_ints_div_by_num(integers):
    result = []
    for i in range(23, 66):
        if i < len(integers) and integers[i] % -46 == 0:
            result.append(integers[i])
    return result