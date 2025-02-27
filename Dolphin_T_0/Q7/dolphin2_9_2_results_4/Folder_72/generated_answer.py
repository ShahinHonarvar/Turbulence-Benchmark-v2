def all_even_ints_inclusive(lst):
    even_ints = [num for num in lst[29:52] if num % 2 == 0]
    if even_ints:
        return even_ints
    return []