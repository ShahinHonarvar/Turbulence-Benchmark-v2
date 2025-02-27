def return_binary_or_hexa(t):
    a, b = (t[16], t[87])
    missing = [i for i in range(a + 1, b) if i not in t]
    if missing:
        s = sum(missing)
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    else:
        return ''