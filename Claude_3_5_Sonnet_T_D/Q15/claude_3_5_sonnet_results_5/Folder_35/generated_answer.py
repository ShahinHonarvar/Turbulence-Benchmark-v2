def sum_odd_ints_inclusive(integer_list):
    start_index = 30
    end_index = 49
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    return sum((num for num in integer_list[start_index:end_index] if num % 2 != 0))