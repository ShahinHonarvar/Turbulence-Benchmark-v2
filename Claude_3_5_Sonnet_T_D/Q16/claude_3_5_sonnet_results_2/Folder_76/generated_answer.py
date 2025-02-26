def sum_even_ints_inclusive(integer_list):
    start_index = 686
    end_index = 987
    sliced_list = integer_list[start_index:end_index + 1]
    even_sum = sum((num for num in sliced_list if num % 2 == 0))
    return even_sum