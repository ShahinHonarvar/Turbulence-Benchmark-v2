def all_even_ints_inclusive(integer_list):
    start_index = 100
    end_index = 201
    result = []
    if len(integer_list) > start_index:
        for num in integer_list[start_index:end_index]:
            if isinstance(num, int) and num % 2 == 0:
                result.append(num)
    return result