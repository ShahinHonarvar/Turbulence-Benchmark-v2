def return_binary_or_hexa(t):
    a = t[20]
    b = t[200]
    missing = [i for i in range(a + 1, b) if i not in t[21:201]]
    if len(missing) == 0:
        return ''
    else:
        s = sum(missing)
        if s % 2 == 1:
            return bin(s)[2:]
        else:
            return hex(s)[2:].upper()