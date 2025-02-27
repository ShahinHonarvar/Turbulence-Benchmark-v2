def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    missing = [i for i in range(a + 1, b) if i not in t]
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]