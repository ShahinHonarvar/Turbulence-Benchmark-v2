def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    missing = [i for i in range(a + 1, b) if i not in t[45:49]]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]