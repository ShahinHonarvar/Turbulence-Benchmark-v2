def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    s = ''
    for i in range(a + 1, b):
        if i not in t[6:8]:
            s += str(i)
    if s != '':
        summ = int(s)
        if summ % 2 == 0:
            return hex(summ)[2:].upper()
        else:
            return bin(summ)[2:]
    else:
        return ''