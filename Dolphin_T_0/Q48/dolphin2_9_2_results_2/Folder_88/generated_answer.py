def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    missing = [x for x in range(a + 1, b) if x not in t[3:10]]
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 0:
            return hex(sum_missing)[2:]
        else:
            return bin(sum_missing)[2:]
    else:
        return ''