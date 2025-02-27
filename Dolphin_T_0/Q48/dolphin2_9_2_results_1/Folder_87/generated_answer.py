def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    s = set(t[20:44])
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