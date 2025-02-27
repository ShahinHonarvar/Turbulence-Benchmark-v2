def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    s = sum(set(range(a + 1, b)) - set(t[25:81]))
    if s % 2 == 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()