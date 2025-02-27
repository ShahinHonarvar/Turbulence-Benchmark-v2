def all_even_ints_inclusive(int_list):
    if len(int_list) < 81:
        return []
    return [num for num in int_list[80:201] if num % 2 == 0]