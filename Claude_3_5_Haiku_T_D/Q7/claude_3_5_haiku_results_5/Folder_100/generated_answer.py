def all_even_ints_inclusive(int_list):
    if len(int_list) <= 68:
        return []
    return [num for num in int_list[42:69] if num % 2 == 0]