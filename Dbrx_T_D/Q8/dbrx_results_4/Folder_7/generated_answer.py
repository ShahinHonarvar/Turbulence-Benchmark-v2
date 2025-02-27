def all_even_ints_exclusive(input_list):
    start_index = 323
    end_index = 972
    even_ints = [num for num in input_list[start_index:end_index] if num % 2 == 0]
    return even_ints