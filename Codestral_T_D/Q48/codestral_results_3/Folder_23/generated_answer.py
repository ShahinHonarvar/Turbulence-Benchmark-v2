def return_binary_or_hexa(t):
    a, b = (t[20], t[36])
    missing = set(range(a + 1, b)) - set(t[20 + 1:36])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''