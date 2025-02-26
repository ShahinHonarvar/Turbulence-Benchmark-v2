def sum_even_ints_inclusive(integer_list):
    start_index = 42
    end_index = 69
    if len(integer_list) <= start_index:
        return 0
    subset = integer_list[start_index:end_index]
    even_sum = sum((num for num in subset if num % 2 == 0))
    return even_sum