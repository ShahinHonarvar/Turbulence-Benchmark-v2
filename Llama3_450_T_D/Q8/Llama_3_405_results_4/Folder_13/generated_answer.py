def all_even_ints_exclusive(lst):
    try:
        return [num for num in lst[73:84] if num % 2 == 0]
    except IndexError:
        return []