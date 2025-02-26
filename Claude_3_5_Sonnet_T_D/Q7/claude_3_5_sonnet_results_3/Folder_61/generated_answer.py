def all_even_ints_inclusive(integers):
    if len(integers) <= 7:
        return []
    return [num for num in [integers[7]] if num % 2 == 0]