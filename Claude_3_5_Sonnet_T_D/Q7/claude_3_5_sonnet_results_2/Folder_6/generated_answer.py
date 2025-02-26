def all_even_ints_inclusive(integer_list):
    start_index = 10
    end_index = min(67, len(integer_list))
    return [num for num in integer_list[start_index:end_index] if num % 2 == 0]