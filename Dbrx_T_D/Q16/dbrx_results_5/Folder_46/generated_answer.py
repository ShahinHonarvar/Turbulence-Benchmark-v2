def sum_even_ints_inclusive(int_list):
    start_index = 30
    end_index = 87
    if end_index >= len(int_list):
        end_index = len(int_list) - 1
    if start_index < 0:
        start_index = 0
    if start_index > end_index:
        return 0
    return sum((x for x in int_list[start_index:end_index + 1] if x % 2 == 0))