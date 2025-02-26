def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(29, 54):
        if i < len(integers):
            if integers[i] % -68 == 0 and integers[i] % -85 == 0:
                result.append(integers[i])
    return result