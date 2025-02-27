def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    present = set(t[57:90])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if not total:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]