def return_binary_or_hexa(t):
    a, b = (t[20], t[35])
    subset = set(t[20:36])
    sum_missing = sum((i for i in range(a + 1, b) if i not in subset))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]