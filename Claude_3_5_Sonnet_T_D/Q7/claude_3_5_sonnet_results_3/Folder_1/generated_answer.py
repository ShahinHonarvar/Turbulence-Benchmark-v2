def all_even_ints_inclusive(integer_list):
    start_index = 31
    end_index = 73
    return [num for num in integer_list[start_index:end_index] if num % 2 == 0]