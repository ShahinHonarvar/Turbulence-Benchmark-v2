def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    missing = [i for i in range(a + 1, b) if i not in t[27:96]]
    s = sum(missing)
    if not missing:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]