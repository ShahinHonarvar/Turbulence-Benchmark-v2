def return_binary_or_hexa(t):
    a = t[13]
    b = t[35]
    s = set(t)
    r = ''
    for i in range(a + 1, b):
        if i not in s:
            r += str(i)
    if len(r) == 0:
        return ''
    if int(r) % 2 != 0:
        return bin(int(r))[2:]
    else:
        return hex(int(r))[2:]