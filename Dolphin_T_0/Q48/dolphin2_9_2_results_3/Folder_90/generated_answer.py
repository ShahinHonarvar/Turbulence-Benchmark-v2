def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    missing_set = set(range(a + 1, b)) - set(t[60:91])
    summ = sum(missing_set)
    if summ % 2 == 0:
        return hex(summ)[2:].upper()
    else:
        return bin(summ)[2:]