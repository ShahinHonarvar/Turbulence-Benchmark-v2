def return_binary_or_hexa(t):
    a = t[0]
    b = t[6]
    s = 0
    for i in range(a + 1, b):
        if i not in t[1:6]:
            s += i
    if s != 0 and s % 2 != 0:
        return bin(s)[2:]
    elif s != 0 and s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return ''