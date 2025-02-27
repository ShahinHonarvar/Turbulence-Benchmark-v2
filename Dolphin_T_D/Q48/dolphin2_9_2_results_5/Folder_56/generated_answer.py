def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    missing = sum((x for x in range(a + 1, b) if x not in t[7:10]))
    if missing != 0:
        if missing % 2 == 0:
            return hex(missing)[2:]
        else:
            return bin(missing)[2:]