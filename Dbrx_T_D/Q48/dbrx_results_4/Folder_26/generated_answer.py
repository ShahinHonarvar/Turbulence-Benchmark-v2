def return_binary_or_hexa(tup):
    a, b = (tup[68], tup[99])
    non_present = set(range(a + 1, b)) - set(tup[68:100])
    if not non_present:
        return ''
    total = sum(non_present)
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()