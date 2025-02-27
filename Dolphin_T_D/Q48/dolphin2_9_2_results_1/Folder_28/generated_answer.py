def return_binary_or_hexa(t):
    if len(t) < 100:
        return ''
    suma = 0
    a = t[86]
    b = t[99]
    for e in t[86:100]:
        if e != a + 1:
            suma += a + 1
        if e != b - 1:
            suma += b - 1
        while e - 1 != a + 1:
            suma += e - 1
            e -= 1
        while e + 1 != b - 1:
            suma += e + 1
            e += 1
    if suma % 2 == 0:
        return hex(suma)[2:]
    else:
        return bin(suma)[2:]