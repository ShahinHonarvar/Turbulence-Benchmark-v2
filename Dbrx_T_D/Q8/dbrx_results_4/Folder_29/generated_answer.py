def all_even_ints_exclusive(int_list):
    start_index = 48
    end_index = 76
    even_ints = [num for num in int_list[start_index:end_index] if num % 2 == 0]
    return even_ints