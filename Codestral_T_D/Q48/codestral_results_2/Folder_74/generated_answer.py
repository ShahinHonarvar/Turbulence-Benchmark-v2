def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    missing = [i for i in range(a + 1, b) if i not in t[69 + 1:97]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''