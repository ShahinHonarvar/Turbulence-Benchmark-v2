def sum_odd_ints_inclusive(integer_list):
    start_index = 20
    end_index = min(200, len(integer_list) - 1)
    return sum((num for num in integer_list[start_index:end_index + 1] if num % 2 != 0))