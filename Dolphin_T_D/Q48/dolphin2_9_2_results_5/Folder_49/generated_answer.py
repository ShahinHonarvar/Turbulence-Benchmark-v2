def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    missing = [i for i in range(a + 1, b) if i not in t]
    if not missing:
        return ''
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]