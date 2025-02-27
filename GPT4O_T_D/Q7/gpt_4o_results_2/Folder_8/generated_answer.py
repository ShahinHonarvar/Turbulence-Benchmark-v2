def all_even_ints_inclusive(lst):
    if 23 < len(lst):
        return [num for num in lst[23:24] if num % 2 == 0]
    return []