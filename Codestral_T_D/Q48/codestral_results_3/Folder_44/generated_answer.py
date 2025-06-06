def return_binary_or_hexa(t):
    a, b = (t[36], t[52])
    missing = set(range(a + 1, b)) - set(t[36 + 1:52])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]