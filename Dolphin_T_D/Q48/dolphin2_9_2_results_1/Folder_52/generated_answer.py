def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    r = [x for x in range(a + 1, b - 1) if x not in t[39:81]]
    s = sum(r)
    if s % 2 != 0:
        return bin(s)[2:]
    elif not r:
        return ''
    else:
        return hex(s)[2:]