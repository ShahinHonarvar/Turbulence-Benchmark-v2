def sum_odd_ints_inclusive(integer_list):
    start_index = 661
    end_index = 924
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list) - 1)
    return sum((num for num in integer_list[start_index:end_index + 1] if num % 2 != 0))