def all_even_ints_inclusive(integer_list):
    if len(integer_list) < 85:
        return []
    return [num for num in integer_list[70:85] if num % 2 == 0]