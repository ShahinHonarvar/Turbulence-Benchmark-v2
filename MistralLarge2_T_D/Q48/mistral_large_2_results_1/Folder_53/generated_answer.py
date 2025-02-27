def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[200:203]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()