def all_odd_ints_inclusive(integer_list):
    start_index = 62
    end_index = 93
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]