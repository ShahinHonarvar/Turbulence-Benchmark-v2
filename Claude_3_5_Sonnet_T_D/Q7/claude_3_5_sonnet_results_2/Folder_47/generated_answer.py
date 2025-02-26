def all_even_ints_inclusive(integer_list):
    start_index = 37
    end_index = 77
    return [num for num in integer_list[start_index:end_index] if num % 2 == 0]