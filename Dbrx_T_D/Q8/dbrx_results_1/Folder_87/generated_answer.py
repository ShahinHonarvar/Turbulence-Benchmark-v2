def all_even_ints_exclusive(int_list):
    if len(int_list) < 100:
        return []
    return [num for num in int_list[32:99:1] if num % 2 == 0]