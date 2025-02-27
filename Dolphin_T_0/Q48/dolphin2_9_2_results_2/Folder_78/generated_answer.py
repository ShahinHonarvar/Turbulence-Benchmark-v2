def return_binary_or_hexa(tuple):
    a = tuple[62]
    b = tuple[96]
    missing_integers = [i for i in range(a + 1, b) if i not in tuple]
    if not missing_integers:
        return ''
    sum_integers = sum(missing_integers)
    if sum_integers % 2 == 0:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:]