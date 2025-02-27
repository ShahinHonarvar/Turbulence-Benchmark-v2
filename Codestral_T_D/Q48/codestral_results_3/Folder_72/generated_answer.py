def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    missing = set(range(a + 1, b)) - set(t[13 + 1:70])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s:
        return hex(s)[2:]
    else:
        return ''