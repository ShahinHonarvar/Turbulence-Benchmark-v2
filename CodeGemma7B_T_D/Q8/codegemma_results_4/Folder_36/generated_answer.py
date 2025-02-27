def all_even_ints_exclusive(lst):
    filtered_ints = [num for num in lst[598:767] if num % 2 == 0]
    return filtered_ints or []