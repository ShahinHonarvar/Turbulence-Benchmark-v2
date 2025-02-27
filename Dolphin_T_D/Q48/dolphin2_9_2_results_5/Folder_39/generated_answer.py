def return_binary_or_hexa(t):
    a, b = (t[44], t[91])
    missing = [x for x in range(a + 1, b) if x not in t]
    summ = sum(missing)
    if summ % 2 == 1:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()