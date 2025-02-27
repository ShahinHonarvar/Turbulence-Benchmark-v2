def all_even_ints_exclusive(int_list):
    filtered_nums = [num for num in int_list[10:79] if num % 2 == 0]
    return filtered_nums or []