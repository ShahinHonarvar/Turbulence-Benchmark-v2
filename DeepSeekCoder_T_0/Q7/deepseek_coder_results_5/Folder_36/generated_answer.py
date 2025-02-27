def all_even_ints_inclusive(lst):
    if 246 >= len(lst) or 750 >= len(lst):
        return []
    return [num for num in lst[246:751] if num % 2 == 0]