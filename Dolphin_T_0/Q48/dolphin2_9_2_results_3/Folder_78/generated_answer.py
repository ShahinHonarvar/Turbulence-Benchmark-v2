def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    missing = [i for i in range(a + 1, b) if i not in t]
    sum_missing = sum(missing)
    if set(missing) == set(range(a + 1, b)):
        return ''
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].lower()