def all_ints_div_by_num(integer_list):
    result = []
    for i in range(319, 613):
        if i < len(integer_list):
            if integer_list[i] % -215 == 0:
                result.append(integer_list[i])
    return result