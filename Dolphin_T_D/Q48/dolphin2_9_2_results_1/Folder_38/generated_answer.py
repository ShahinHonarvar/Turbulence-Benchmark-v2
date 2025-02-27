def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    missing = [i for i in range(a + 1, b) if i not in t]
    if missing:
        s = sum(missing)
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:].upper()
    else:
        return ''