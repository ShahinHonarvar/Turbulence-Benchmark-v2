def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    summ = sum(set(range(a + 1, b)) - set(t[2:8]))
    if summ % 2:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()