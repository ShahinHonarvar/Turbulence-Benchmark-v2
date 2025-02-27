def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(40, 201):
        if integers[i] % 21 == 0 and integers[i] % 71 == 0:
            result.append(integers[i])
    return result