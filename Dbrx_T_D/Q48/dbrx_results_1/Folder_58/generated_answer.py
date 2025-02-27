def return_binary_or_hexa(t):
    a, b = (t[275], t[871])
    missing = set(range(a + 1, b)) - set(t[275:872])
    if not missing:
        return ''
    total = sum(missing)
    return bin(total)[2:] if total & 1 else hex(total)[2:].upper()