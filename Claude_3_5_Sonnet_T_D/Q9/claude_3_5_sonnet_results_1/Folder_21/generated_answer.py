def all_odd_ints_inclusive(integer_list):
    start_index = 639
    end_index = 976
    if len(integer_list) <= start_index:
        return []
    sliced_list = integer_list[start_index:end_index]
    return [num for num in sliced_list if num % 2 != 0]