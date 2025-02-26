def sum_even_ints_inclusive(integer_list):
    start_index = 90
    end_index = 200
    if len(integer_list) <= start_index:
        return 0
    range_end = min(end_index + 1, len(integer_list))
    return sum((num for num in integer_list[start_index:range_end] if num % 2 == 0))