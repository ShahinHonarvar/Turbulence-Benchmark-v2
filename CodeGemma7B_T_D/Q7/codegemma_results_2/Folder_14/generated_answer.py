def all_even_ints_inclusive(list_ints):
    if not any((num % 2 == 0 for num in list_ints[5:8])):
        return []
    return list_ints[5:8:2]