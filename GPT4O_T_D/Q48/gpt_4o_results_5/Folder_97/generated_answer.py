def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    sum_missing = sum((x for x in range(a + 1, b) if x not in t[34:70]))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]