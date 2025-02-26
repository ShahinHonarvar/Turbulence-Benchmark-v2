def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(86, 91):
        if i < len(integer_list):
            if integer_list[i] % -71 == 0 and integer_list[i] % -67 == 0:
                result.append(integer_list[i])
    return result