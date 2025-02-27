def return_binary_or_hexa(t):
    if not t or len(t) < 349:
        return ''
    a = t[110]
    b = t[348]
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()