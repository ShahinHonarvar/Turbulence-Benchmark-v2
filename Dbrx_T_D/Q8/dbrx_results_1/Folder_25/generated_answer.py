def all_even_ints_exclusive(int_list):
    start_index = 41
    end_index = 69
    return [num for num in int_list[start_index:end_index] if num % 2 == 0]