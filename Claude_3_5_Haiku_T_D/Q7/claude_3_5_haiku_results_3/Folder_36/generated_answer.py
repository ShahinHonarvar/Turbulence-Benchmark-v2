def all_even_ints_inclusive(lst):
    if len(lst) <= 750:
        return []
    return [num for num in lst[246:751] if num % 2 == 0]