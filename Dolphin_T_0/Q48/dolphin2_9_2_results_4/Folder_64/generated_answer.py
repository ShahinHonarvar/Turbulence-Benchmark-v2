def return_binary_or_hexa(t):
    a = t[0]
    b = t[5]
    r = [i for i in range(a + 1, b) if i not in t]
    s = sum(r)
    if s != 0:
        if s % 2 != 0:
            return bin(s).replace('0b', '')
        else:
            return hex(s).replace('0x', '')
    else:
        return ''