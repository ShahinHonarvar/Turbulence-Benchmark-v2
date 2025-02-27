def return_binary_or_hexa(x):
    a = x[20]
    b = x[43]
    if all((i in x[21:43] for i in range(a + 1, b))):
        return ''
    s = sum((i for i in range(a + 1, b) if i not in x[21:43]))
    if s % 2 == 0:
        return hex(s).replace('0x', '')
    else:
        return bin(s)[2:]