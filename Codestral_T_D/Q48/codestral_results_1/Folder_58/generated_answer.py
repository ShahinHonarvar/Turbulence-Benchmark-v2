def return_binary_or_hexa(t):
    a, b = (t[275], t[871])
    t_slice = set(t[276:871])
    missing = set(range(a + 1, b)) - t_slice
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''