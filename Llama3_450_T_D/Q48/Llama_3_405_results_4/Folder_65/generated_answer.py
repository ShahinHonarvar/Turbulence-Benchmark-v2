def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    s = set(t[51:77])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]