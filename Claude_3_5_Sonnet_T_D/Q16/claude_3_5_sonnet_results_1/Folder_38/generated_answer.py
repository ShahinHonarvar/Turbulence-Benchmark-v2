def sum_even_ints_inclusive(integer_list):
    start_index = 22
    end_index = 63
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list) - 1)
    even_sum = sum((num for num in integer_list[start_index:end_index + 1] if num % 2 == 0))
    return even_sum