def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    missing = [i for i in range(a + 1, b) if i not in t]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]