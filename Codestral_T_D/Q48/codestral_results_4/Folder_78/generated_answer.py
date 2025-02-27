def return_binary_or_hexa(tup):
    a, b = (tup[62], tup[96])
    missing = set(range(a + 1, b)) - set(tup[62 + 1:96])
    if missing:
        total = sum(missing)
        return bin(total)[2:] if total % 2 else hex(total)[2:].upper()
    return ''