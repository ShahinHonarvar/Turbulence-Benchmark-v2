def return_binary_or_hexa(t):
    a, b = (t[427], t[669])
    s = sum(set(range(a + 1, b)) - set(t[428:669]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()