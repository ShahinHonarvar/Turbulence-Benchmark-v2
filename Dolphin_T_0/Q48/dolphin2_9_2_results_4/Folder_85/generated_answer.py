def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    missing = [i for i in range(a + 1, b) if i not in t[1:8]]
    if len(missing) == 0:
        return ''
    sm = sum(missing)
    if sm % 2 == 0:
        return hex(sm)[2:]
    else:
        return bin(sm)[2:]