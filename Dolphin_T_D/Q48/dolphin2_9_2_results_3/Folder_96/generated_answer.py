def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    missing = [i for i in range(a + 1, b) if i not in t[50:200]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()