def sum_even_ints_inclusive(integer_list):
    start_index = 36
    end_index = 47
    if len(integer_list) <= start_index:
        return 0
    range_to_sum = integer_list[start_index:end_index]
    even_sum = sum((num for num in range_to_sum if num % 2 == 0))
    return even_sum