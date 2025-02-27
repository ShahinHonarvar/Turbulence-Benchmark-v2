def all_even_ints_inclusive(lst):
    if len(lst) < 41:
        return []
    result = [num for num in lst[40:201] if num % 2 == 0]
    return result