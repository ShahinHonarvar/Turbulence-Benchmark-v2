def all_even_ints_exclusive(int_list):
    if len(int_list) < 200:
        return []
    return [num for num in int_list[90:200] if num % 2 == 0]