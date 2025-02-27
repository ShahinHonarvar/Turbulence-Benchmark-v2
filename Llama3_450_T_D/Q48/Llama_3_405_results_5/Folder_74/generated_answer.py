def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    s = set(range(a + 1, b))
    missing = s - set(t[70:97])
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]