def return_binary_or_hexa(t):
    a, b = (t[275], t[871])
    missing = [x for x in range(a + 1, b) if x not in t]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]