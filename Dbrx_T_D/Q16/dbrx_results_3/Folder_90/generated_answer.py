def sum_even_ints_inclusive(int_list):
    start_index = 262
    end_index = 746
    if start_index < 0 or end_index >= len(int_list) or start_index > end_index:
        return 0
    return sum((x for x in int_list[start_index:end_index + 1] if x % 2 == 0))