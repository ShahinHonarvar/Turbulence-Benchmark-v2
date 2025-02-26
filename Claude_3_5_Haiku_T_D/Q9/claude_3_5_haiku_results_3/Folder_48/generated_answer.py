def all_odd_ints_inclusive(lst):
    if len(lst) <= 605:
        return []
    return [num for num in lst[533:606] if num % 2 != 0]