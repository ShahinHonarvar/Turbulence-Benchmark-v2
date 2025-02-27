def sum_even_ints_inclusive(lst):
    if not any((i % 2 == 0 for i in lst[31:35])):
        return 0
    return sum((i for i in lst[31:35] if i % 2 == 0))