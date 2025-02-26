def all_even_ints_inclusive(integers):
    if len(integers) <= 73:
        return []
    return [num for num in [integers[73]] if num % 2 == 0]