def all_even_ints_inclusive(integer_list):
    if len(integer_list) <= 73:
        return []
    if integer_list[73] % 2 == 0:
        return [integer_list[73]]
    return []