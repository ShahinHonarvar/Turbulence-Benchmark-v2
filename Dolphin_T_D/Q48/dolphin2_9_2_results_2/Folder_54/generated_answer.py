def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    s = sum(range(a + 1, b)) - sum(t[35:65])
    if a != b - 1:
        if s % 2 == 0:
            return hex(s)[2:]
        else:
            return bin(s)[2:]
    else:
        return ''