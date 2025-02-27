def all_even_ints_exclusive(list_of_ints):
    if len(list_of_ints) < 98:
        return []
    return [num for num in list_of_ints[70:98] if num % 2 == 0]