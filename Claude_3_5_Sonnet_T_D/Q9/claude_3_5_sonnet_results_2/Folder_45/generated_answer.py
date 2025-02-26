def all_odd_ints_inclusive(integer_list):
    start_index = 30
    end_index = 201
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]