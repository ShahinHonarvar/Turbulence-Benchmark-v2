def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    missing = [i for i in range(a + 1, b) if i not in t]
    if len(missing) == 0:
        return ''
    else:
        sum_missing = sum(missing)
        if sum_missing % 2:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:].upper()