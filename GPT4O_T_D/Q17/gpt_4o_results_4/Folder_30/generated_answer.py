def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(11, min(77, len(integers))):
        if integers[i] % -81 == 0 and integers[i] % -94 == 0:
            result.append(integers[i])
    return result