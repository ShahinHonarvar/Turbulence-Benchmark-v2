def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    missing = set(range(a + 1, b)) - set(t[1:8])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]