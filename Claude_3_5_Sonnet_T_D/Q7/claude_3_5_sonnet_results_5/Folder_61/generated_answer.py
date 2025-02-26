def all_even_ints_inclusive(integer_list):
    if len(integer_list) <= 7:
        return []
    return [num for num in [integer_list[7]] if num % 2 == 0]