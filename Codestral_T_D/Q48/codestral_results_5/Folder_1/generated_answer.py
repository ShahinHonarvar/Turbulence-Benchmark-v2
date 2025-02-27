def return_binary_or_hexa(t):
    a, b = (t[17], t[88])
    missing = [i for i in range(a + 1, b) if i not in t[17:89]]
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''