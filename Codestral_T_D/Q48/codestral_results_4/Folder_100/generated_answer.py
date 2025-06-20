def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    missing = set(range(a + 1, b)) - set(t[44 + 1:78])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]