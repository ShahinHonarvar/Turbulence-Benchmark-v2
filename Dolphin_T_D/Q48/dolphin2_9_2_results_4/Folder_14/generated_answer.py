def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    m = sum([i for i in range(a + 1, b) if i not in t[3:6]])
    if m == 0:
        return ''
    elif m % 2:
        return bin(m)[2:]
    else:
        return hex(m)[2:].upper()