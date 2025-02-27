def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(86, 91):
        if i < len(integers) and integers[i] % 71 == 0 and (integers[i] % 67 == 0):
            result.append(integers[i])
    return result