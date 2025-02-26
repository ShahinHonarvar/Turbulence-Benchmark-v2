def all_even_ints_inclusive(integer_list):
    start_index = 29
    end_index = 80
    result = []
    if len(integer_list) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result