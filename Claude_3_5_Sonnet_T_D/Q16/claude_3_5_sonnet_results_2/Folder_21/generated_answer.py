def sum_even_ints_inclusive(integer_list):
    start_index = 639
    end_index = 975
    if len(integer_list) <= start_index:
        return 0
    actual_end = min(end_index, len(integer_list) - 1)
    return sum((num for num in integer_list[start_index:actual_end + 1] if num % 2 == 0))