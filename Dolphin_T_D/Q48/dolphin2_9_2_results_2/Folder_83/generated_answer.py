def return_binary_or_hexa(t):
    a = t[90]
    b = t[200]
    elements = set(t[90:201])
    s = 0
    for i in range(a + 1, b):
        if i not in elements:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]