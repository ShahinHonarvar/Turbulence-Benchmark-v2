def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    missing = [i for i in range(a + 1, b) if i not in t[2:7]]
    if not missing:
        return ''
    else:
        s = sum(missing)
        if s % 2 == 1:
            return bin(s)[2:]
        else:
            return hex(s)[2:].upper()