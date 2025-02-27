def all_even_ints_exclusive(int_list):
    if not any((num % 2 == 0 for num in int_list[64:80])):
        return []
    return [num for num in int_list[64:80] if num % 2 == 0]