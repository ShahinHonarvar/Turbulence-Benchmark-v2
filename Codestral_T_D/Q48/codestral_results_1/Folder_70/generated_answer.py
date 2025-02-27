def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    s = sum(set(range(a + 1, b)) - set(t[43 + 1:70]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''