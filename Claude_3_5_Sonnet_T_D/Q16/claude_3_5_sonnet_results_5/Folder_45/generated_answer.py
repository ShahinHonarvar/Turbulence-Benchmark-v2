def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 31:
        return 0
    end_index = min(201, len(integer_list))
    return sum((num for num in integer_list[30:end_index] if num % 2 == 0))