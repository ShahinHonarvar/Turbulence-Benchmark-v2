def all_odd_ints_inclusive(integer_list):
    start_index = 75
    end_index = 86
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]