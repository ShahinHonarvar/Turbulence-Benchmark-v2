def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    missing = [x for x in range(a + 1, b) if x not in t[18:53]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]