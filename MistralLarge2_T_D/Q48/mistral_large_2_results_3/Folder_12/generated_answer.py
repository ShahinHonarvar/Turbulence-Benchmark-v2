def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    sum_missing = sum(set(range(a + 1, b)).difference(t[16:88]))
    if sum_missing == 0:
        return ''
    else:
        return bin(sum_missing)[2:] if sum_missing % 2 != 0 else hex(sum_missing)[2:].upper()