def all_odd_ints_inclusive(integer_list):
    start_index = 56
    end_index = 83
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]