def return_binary_or_hexa(t):
    a, b = (t[73], t[84])
    s = sum((i for i in range(a + 1, b) if i not in t[74:84]))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()