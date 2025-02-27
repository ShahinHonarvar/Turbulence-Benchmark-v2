def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    missing = [i for i in range(a + 1, b) if i not in t]
    if len(missing) == 0:
        return ''
    sum_missing = sum(missing)
    return bin(sum_missing)[2:] if sum_missing % 2 == 1 else hex(sum_missing)[2:]