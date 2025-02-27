def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    missing = [x for x in range(a + 1, b) if x not in t[3:10]]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]