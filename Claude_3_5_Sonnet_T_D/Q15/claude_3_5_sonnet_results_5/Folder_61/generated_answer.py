def sum_odd_ints_inclusive(integer_list):
    end_index = min(8, len(integer_list))
    return sum((num for num in integer_list[:end_index] if num % 2 != 0))