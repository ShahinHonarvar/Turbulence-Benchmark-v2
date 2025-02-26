def all_odd_ints_inclusive(integer_list):
    start_index = 661
    end_index = 925
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]