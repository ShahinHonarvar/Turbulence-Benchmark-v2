def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(56, 89):
        if i < len(integers):
            if integers[i] % -59 == 0 and integers[i] % -79 == 0:
                result.append(integers[i])
    return result