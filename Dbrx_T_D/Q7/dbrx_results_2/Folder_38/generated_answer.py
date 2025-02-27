def all_even_ints_inclusive(lst):
    if not lst or len(lst) < 63:
        return []
    return [num for num in lst[22:64] if num % 2 == 0]