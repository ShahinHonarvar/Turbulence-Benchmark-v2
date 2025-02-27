def return_binary_or_hexa(t):
    a, b = (t[62], t[96])
    s = sum((i for i in range(a + 1, b) if i not in set(t[62:97])))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]