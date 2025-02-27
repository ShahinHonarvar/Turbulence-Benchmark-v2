def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    missing = [i for i in range(a + 1, b) if i not in t[16:87]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]