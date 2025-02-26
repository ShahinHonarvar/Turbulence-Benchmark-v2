def sum_even_ints_inclusive(integer_list):
    if len(integer_list) <= 29:
        return 0
    end_index = min(52, len(integer_list))
    relevant_range = integer_list[29:end_index]
    even_sum = sum((num for num in relevant_range if num % 2 == 0))
    return even_sum