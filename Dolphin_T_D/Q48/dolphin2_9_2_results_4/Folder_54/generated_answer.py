def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[35]
    b = tuple_of_integers[64]
    missing = [i for i in range(a + 1, b) if i not in tuple_of_integers[35:65]]
    total = sum(missing)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower() if total != 0 else ''