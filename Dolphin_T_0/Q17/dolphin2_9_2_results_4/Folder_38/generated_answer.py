def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(10, 77):
        if integers[i] % -40 == 0 and integers[i] % -12 == 0:
            result.append(integers[i])
    return result