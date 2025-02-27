def all_odd_ints_inclusive(int_list):
    if not any((n % 2 for n in int_list[527:539])):
        return []
    return [n for n in int_list[527:539] if n % 2]