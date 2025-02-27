def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    s = sum(range(a + 1, b)) - sum(t[39:81])
    if s == 0:
        return ''
    if s % 2 == 0:
        return hex(s)[2:].upper()
    return bin(s)[2:]