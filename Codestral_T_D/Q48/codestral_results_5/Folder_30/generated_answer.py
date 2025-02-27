def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    missing = [i for i in range(a + 1, b) if i not in t[22:25]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''