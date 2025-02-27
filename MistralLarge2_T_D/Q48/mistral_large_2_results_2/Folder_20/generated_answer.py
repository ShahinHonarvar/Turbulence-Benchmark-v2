def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    existing_set = set(t[27:97])
    sum_missing = sum((x for x in range(a + 1, b) if x not in existing_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]