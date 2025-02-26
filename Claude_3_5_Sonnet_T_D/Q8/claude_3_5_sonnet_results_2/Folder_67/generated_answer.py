def all_even_ints_exclusive(integer_list):
    if len(integer_list) <= 50:
        return []
    start_index = 50
    end_index = min(74, len(integer_list) - 1)
    result = []
    for i in range(start_index, end_index):
        if integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result