def return_binary_or_hexa(t):
    a = t[90]
    b = t[200]
    s = sum(range(a + 1, b)) - sum(t[91:200])
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()