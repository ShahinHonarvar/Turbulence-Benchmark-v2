def return_binary_or_hexa(t):
    a = t[0]
    b = t[6]
    summ = sum((i for i in range(a + 1, b) if i not in t[1:6]))
    if summ % 2 != 0:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()