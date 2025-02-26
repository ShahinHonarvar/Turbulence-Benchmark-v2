def all_odd_ints_inclusive(integer_list):
    start_index = 55
    end_index = 99
    if len(integer_list) <= start_index:
        return []
    end_index = min(end_index, len(integer_list))
    return [num for num in integer_list[start_index:end_index] if num % 2 != 0]