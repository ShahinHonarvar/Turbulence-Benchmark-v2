def all_even_ints_inclusive(int_list):
    if len(int_list) <= 71:
        return []
    even_ints = [num for num in int_list[52:72] if num % 2 == 0]
    return even_ints