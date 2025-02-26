def all_odd_ints_inclusive(int_list):
    start_index = 246
    end_index = 751
    return [num for num in int_list[start_index:end_index] if num % 2 != 0]