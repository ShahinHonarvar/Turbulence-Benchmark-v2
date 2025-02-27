def all_even_ints_exclusive(in_list):
    if len(in_list) < 2:
        return []
    return [num for num in in_list[:2] if num % 2 == 0]