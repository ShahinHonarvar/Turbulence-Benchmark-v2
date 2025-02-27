def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    missing = [i for i in range(a + 1, b) if i not in t[29:53 + 1]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]