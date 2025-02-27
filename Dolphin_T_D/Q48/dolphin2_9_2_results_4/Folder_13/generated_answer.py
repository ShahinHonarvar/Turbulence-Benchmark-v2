def return_binary_or_hexa(t):
    a = t[46]
    b = t[91]
    s = sum(range(a + 1, b)) - sum(t[47:91])
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()