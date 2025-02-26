def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(20, 36):
        if i < len(integers):
            if integers[i] % -36 == 0 and integers[i] % -89 == 0:
                result.append(integers[i])
    return result