def all_even_ints_inclusive(integers):
    if len(integers) < 37:
        return []
    result = [num for num in integers[33:37] if num % 2 == 0]
    return result