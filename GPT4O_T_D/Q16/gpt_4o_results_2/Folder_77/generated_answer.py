def sum_even_ints_inclusive(int_list):
    if len(int_list) < 539:
        return 0
    return sum((i for i in int_list[527:539] if i % 2 == 0))