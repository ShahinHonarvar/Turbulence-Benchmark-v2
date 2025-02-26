def all_even_ints_exclusive(integers):
    if len(integers) <= 95:
        return []
    result = [num for num in integers[94:95] if num % 2 == 0]
    return result