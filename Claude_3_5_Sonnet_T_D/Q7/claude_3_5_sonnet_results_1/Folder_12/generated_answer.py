def all_even_ints_inclusive(integer_list):
    if len(integer_list) < 15:
        return []
    end_index = min(65, len(integer_list))
    return [num for num in integer_list[14:end_index] if num % 2 == 0]