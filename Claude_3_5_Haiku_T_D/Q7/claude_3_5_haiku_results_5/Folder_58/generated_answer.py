def all_even_ints_inclusive(integers):
    if len(integers) <= 556:
        return []
    even_subset = [num for num in integers[209:557] if num % 2 == 0]
    return even_subset