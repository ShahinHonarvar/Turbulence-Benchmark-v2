def all_even_ints_inclusive(integers):
    start_index = 13
    end_index = 69
    return [num for num in integers[start_index:end_index] if num % 2 == 0]