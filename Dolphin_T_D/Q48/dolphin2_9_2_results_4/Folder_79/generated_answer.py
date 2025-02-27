def return_binary_or_hexa(tuple):
    a, b = (tuple[1], tuple[7])
    present_integers = set(tuple[2:7])
    missed_integers = [i for i in range(a + 1, b) if i not in present_integers]
    total = sum(missed_integers)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()