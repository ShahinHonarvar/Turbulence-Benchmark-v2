def all_even_ints_inclusive(integer_list):
    start_index = 90
    end_index = 201
    sliced_list = integer_list[start_index:end_index]
    return [num for num in sliced_list if num % 2 == 0]