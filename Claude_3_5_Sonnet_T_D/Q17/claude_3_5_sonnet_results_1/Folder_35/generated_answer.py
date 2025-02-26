def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(77, 88):
        if i < len(integers):
            if integers[i] % 23 == 0 and integers[i] % 57 == 0:
                result.append(integers[i])
    return result