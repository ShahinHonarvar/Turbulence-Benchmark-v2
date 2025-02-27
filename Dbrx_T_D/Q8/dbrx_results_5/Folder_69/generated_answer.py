def all_even_ints_exclusive(lst):
    if len(lst) < 100:
        return []
    return [num for num in lst[68:99] if num % 2 == 0]