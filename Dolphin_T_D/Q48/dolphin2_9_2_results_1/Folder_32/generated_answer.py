def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    missing = [i for i in range(a + 1, b) if i not in t[87:89]]
    summ = sum(missing)
    if summ % 2 == 0:
        return hex(summ)
    else:
        return bin(summ)[2:]