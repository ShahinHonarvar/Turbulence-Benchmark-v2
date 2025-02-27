def sum_even_ints_inclusive(seq):
    if not any((num % 2 == 0 for num in seq[75:86])):
        return 0
    return sum((num for num in seq[75:86] if num % 2 == 0))