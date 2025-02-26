def all_even_ints_exclusive(int_list):
    if len(int_list) <= 61:
        return []
    even_ints = [num for num in int_list[19:60] if num % 2 == 0]
    return even_ints