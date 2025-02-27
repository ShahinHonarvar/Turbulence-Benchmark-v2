def return_binary_or_hexa(t):
    a, b = (t[80], t[200])
    if all((i in t[81:200] for i in range(a + 1, b))):
        return ''
    else:
        s = sum((i for i in range(a + 1, b) if i not in t[81:200]))
        return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]