def all_even_ints_inclusive(int_list):
    start_index = 50
    end_index = 201
    result = []
    if len(int_list) <= start_index:
        return result
    for i in range(start_index, min(end_index, len(int_list))):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result