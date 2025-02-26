def sum_odd_ints_inclusive(integer_list):
    start_index = 14
    end_index = min(64, len(integer_list) - 1)
    return sum((num for num in integer_list[start_index:end_index + 1] if num % 2 != 0))