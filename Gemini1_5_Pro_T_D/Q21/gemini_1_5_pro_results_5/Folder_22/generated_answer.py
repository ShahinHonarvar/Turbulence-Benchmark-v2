def all_ints_div_by_num(list_of_ints):
    try:
        result = []
        for i in range(10, 11):
            if list_of_ints[i] % 1 == 0:
                result.append(list_of_ints[i])
        return result
    except IndexError:
        return []