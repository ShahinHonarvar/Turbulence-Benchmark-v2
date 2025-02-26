def all_odd_ints_inclusive(integer_list):
    start_index = 66
    end_index = 94
    if len(integer_list) <= start_index:
        return []
    subset = integer_list[start_index:end_index]
    return [num for num in subset if num % 2 != 0]