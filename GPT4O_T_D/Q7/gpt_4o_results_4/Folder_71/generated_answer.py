def all_even_ints_inclusive(integers):
    if len(integers) < 53:
        return []
    return [num for num in integers[26:53] if num % 2 == 0]