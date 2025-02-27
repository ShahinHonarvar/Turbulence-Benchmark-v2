def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[57:88]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]