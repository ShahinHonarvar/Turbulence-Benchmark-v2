def sum_odd_ints_inclusive(int_list):
    if not int_list or len(int_list) < 539:
        return 0
    return sum((x for x in int_list[527:539] if x % 2 != 0))