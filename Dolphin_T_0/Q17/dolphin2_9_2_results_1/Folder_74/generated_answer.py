def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(90, 98):
        if i < len(ints):
            if ints[i] % 13 == 0 and ints[i] % 35 == 0:
                result.append(ints[i])
    return result