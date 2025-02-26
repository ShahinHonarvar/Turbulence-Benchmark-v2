def sum_even_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list))
    relevant_slice = integer_list[start_index:end_index]
    even_sum = sum((num for num in relevant_slice if num % 2 == 0))
    return even_sum