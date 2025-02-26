def all_even_ints_inclusive(int_list):
    if len(int_list) < 67:
        return []
    even_subset = [num for num in int_list[56:67] if num % 2 == 0]
    return even_subset