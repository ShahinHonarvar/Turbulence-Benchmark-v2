def all_even_ints_exclusive(int_list):
    if len(int_list) <= 2:
        return []
    return [num for num in int_list[1:-1] if num % 2 == 0]