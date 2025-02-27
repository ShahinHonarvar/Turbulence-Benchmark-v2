def sum_even_ints_inclusive(integers):
    if not integers or len(integers) < 539:
        return 0
    even_sum = sum((x for x in integers[527:539] if x % 2 == 0))
    return even_sum