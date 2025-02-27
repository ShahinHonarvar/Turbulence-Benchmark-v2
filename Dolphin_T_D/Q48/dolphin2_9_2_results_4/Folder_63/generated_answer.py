def return_binary_or_hexa(tuple):
    a = tuple[81]
    b = tuple[86]
    existing = set(tuple[82:86])
    missing = [i for i in range(a + 1, b) if i not in existing]
    s = sum(missing)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]