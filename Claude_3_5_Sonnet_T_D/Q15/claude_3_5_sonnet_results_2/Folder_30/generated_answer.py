def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) <= 55:
        return 0
    end_index = min(99, len(integer_list))
    return sum((num for num in integer_list[55:end_index] if num % 2 != 0))