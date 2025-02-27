def return_binary_or_hexa(t):
    a, b = (t[70], t[98])
    s = sum(set(range(a + 1, b)) - set(t[71:98]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:] if s != 0 else ''