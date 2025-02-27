def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    summ = sum([x for x in range(a + 1, b) if x not in t])
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]