def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    lo = a + 1
    hi = b - 1
    missing = 0
    for x in range(lo, hi + 1):
        if not x in t[0:4]:
            missing += x
    if missing % 2:
        return bin(missing)[2:]
    return hex(missing)[2:].upper()