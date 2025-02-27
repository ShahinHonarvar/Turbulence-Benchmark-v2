def all_even_ints_inclusive(integers):
    if len(integers) < 8:
        return []
    sublist = integers[7:8]
    return [num for num in sublist if num % 2 == 0]