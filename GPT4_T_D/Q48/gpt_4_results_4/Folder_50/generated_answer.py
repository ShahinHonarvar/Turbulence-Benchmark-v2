def return_binary_or_hexa(tuple):
    a, b = (tuple[13], tuple[76])
    missing_integers = set(range(a + 1, b)) - set(tuple[14:76])
    sum_missing