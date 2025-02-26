def all_even_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    result = []
    if len(integer_list) > start_index:
        for i in range(start_index, min(end_index, len(integer_list))):
            if integer_list[i] % 2 == 0:
                result.append(integer_list[i])
    return result