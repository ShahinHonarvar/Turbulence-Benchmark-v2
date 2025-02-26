def sum_even_ints_inclusive(integer_list):
    start_index = 14
    end_index = 65
    if len(integer_list) <= start_index:
        return 0
    truncated_list = integer_list[start_index:end_index]
    even_numbers = [num for num in truncated_list if num % 2 == 0]
    return sum(even_numbers)