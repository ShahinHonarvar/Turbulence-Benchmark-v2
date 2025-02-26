def all_even_ints_exclusive(lst):
    if len(lst) <= 984:
        return []
    even_ints = [num for num in lst[370:983] if num % 2 == 0]
    return even_ints