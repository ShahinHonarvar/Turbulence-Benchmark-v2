def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    summ = 0
    for i in range(a + 1, b):
        if i not in t[18:61]:
            summ += i
    if summ % 2 != 0:
        return str(bin(summ))[2:]
    else:
        return hex(summ)[2:].upper()