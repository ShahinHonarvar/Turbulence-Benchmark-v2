def all_even_ints_inclusive(integers):
    if len(integers) <= 94:
        return []
    return [num for num in integers[75:95] if num % 2 == 0]