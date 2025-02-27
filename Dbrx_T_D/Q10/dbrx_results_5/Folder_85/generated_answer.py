def all_odd_ints_exclusive(input_list):
    result = []
    if len(input_list) >= 6:
        for i in range(4, 6):
            if input_list[i] % 2 != 0:
                result.append(input_list[i])
    return result