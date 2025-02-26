def sum_even_ints_inclusive(integer_list):
    start_index = 262
    end_index = 746
    sliced_list = integer_list[start_index:end_index + 1]
    even_sum = sum((num for num in sliced_list if num % 2 == 0))
    return even_sum