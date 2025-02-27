def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    sum_missing = sum(set(range(a + 1, b)) - set(t[51:77]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]