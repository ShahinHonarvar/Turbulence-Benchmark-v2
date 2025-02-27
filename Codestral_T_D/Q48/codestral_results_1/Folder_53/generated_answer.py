def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    s = sum(set(range(a + 1, b)) - set(t[200 + 1:202]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0') if s else ''