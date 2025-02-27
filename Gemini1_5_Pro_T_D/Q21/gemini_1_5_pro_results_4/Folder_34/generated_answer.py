def all_ints_div_by_num(list_of_ints):
    result = []
    if len(list_of_ints) > 30:
        for i in range(30, 31):
            if list_of_ints[i] % 3 == 0:
                result.append(list_of_ints[i])
        return result
    else:
        return result