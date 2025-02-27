def return_binary_or_hexa(t):
    a, b = (t[77], t[84])
    s = sum((i for i in range(a + 1, b) if i not in t[77:84]))
    return bin(s).lstrip('0b') if s % 2 else hex(s).lstrip('0x').lstrip('0')