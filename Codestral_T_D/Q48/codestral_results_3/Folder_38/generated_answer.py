def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    missing = [x for x in range(a + 1, b) if x not in t[36 + 1:85]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''