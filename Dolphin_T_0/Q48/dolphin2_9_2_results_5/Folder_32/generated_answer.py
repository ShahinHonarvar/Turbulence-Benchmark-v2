def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    s = 0
    for i in range(a + 1, b):
        if i not in t[87:90]:
            s += i
    if s % 2 == 0:
        return hex(s).replace('0x', '')
    else:
        return bin(s).replace('0b', '')