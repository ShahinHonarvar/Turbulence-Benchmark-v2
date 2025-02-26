def all_even_ints_inclusive(integer_list):
    start_index = 27
    end_index = 56
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    return [num for num in integer_list[start_index:end_index] if num % 2 == 0]