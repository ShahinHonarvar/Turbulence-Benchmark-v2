def all_odd_ints_inclusive(input_list):
    result = []
    for i in range(min(34, len(input_list)), min(56, len(input_list))):
        if input_list[i] % 2 != 0:
            result.append(input_list[i])
    return result