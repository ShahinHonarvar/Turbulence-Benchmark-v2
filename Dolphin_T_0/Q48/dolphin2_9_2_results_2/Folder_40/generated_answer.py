def return_binary_or_hexa(t):
    a, _, _, b = t
    missing = [x for x in range(a + 1, b) if x not in t]
    result = sum(missing)
    if result % 2:
        return bin(result)[2:]
    else:
        return hex(result)[2:]