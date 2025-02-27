def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    sum_missing = sum((x for x in range(a + 1, b) if x not in set(t[44:92])))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 == 1 else hex(sum_missing)[2:]