def return_binary_or_hexa(t):
    a, _, b = t
    s = sum((i for i in range(a + 1, b) if i not in t))
    return bin(s).replace('0b', '') if s % 2 else hex(s).replace('0x', '') if s != 0 else ''