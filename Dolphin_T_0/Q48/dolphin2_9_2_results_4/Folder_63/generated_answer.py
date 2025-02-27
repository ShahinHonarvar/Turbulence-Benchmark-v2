def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    missing = [x for x in range(a + 1, b) if x not in t[81:86]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]