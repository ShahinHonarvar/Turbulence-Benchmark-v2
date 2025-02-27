def all_even_ints_inclusive(int_list):
    if not any((num % 2 == 0 for num in int_list[0:5])):
        return []
    return [num for num in int_list[0:5] if num % 2 == 0]