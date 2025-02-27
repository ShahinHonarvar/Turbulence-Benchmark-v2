def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    s = sum((i for i in range(a + 1, b) if i not in t[1:6]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 == 1 else hex(s)[2:]