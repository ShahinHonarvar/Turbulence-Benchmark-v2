def all_even_ints_inclusive(lst):
    if len(lst) <= 73:
        return []
    evens = [num for num in lst[73:74] if num % 2 == 0]
    return evens