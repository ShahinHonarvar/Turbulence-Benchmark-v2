def all_odd_ints_inclusive(input_list):
    result = []
    for i in range(62, 79):
        if i % 2 != 0:
            result.append(input_list[i])
    return result