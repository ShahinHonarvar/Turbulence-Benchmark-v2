def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    sum_missing = sum(set(range(a + 1, b)) - set(t[19:33]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()