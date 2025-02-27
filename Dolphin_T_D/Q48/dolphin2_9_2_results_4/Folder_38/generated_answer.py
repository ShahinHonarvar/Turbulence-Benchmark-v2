def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    integers = t[36:86]
    s = sum(set(range(a + 1, b + 1)) - set(integers))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]