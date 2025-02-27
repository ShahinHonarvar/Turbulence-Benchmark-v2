def all_odd_ints_inclusive(input_list):
    if len(input_list) < 63:
        return []
    result = []
    for i in range(22, 64):
        if input_list[i] % 2 != 0:
            result.append(input_list[i])
    return result