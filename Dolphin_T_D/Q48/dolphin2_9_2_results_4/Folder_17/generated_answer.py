def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    missing = [i for i in range(a + 1, b) if i not in t[73:85]]
    if not missing:
        return ''
    summ = sum(missing)
    if summ % 2:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:]