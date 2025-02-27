def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    missing = [x for x in range(a + 1, b) if x not in t[11:77]]
    summ = sum(missing)
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]