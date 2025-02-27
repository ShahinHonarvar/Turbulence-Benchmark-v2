def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    missing = [x for x in range(a + 1, b) if x not in t[18:60]]
    sum_missing = sum(missing) if missing else 0
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]