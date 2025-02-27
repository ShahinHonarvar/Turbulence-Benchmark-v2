def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    excluded = [i for i in range(a + 1, b) if i not in t]
    s = sum(excluded)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()