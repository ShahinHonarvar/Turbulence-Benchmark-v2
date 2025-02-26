def all_even_ints_exclusive(integers):
    if len(integers) < 3:
        return []
    return [num for num in integers[1:-1] if num % 2 == 0]