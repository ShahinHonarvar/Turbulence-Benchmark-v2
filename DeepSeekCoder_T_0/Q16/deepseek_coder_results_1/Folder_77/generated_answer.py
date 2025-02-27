def sum_even_ints_inclusive(int_list):
    if 527 <= len(int_list) - 1 < 538:
        return sum((x for x in int_list[527:538 + 1] if x % 2 == 0))
    return 0