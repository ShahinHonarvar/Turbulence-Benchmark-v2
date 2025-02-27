def return_binary_or_hexa(t):
    a, b = (t[36], t[54])
    present = set(t[36:55])
    s = sum((i for i in range(a + 1, b) if i not in present))
    if all((i in present for i in range(a + 1, b))):
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()