def sum_odd_ints_inclusive(integer_list):
    start_index = 30
    end_index = 88
    if len(integer_list) <= start_index:
        return 0
    range_end = min(end_index, len(integer_list))
    return sum((num for num in integer_list[start_index:range_end] if num % 2 != 0))