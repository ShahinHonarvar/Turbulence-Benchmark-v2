def all_even_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst) if num % 2 == 0 and i > 100 and (i < 101)]
    if result:
        return result
    else:
        return []