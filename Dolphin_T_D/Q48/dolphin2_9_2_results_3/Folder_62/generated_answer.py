def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    present = [i for i in t[50:93]]
    missing = [x for x in range(a + 1, b) if x not in present]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]