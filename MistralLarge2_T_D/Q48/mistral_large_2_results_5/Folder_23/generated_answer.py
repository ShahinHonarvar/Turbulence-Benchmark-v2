def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    subset = set(t[21:36])
    sum_missing = sum((i for i in range(a + 1, b) if i not in subset))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()