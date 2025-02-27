def return_binary_or_hexa(t):
    a, b = (t[2], t[7])
    missing = [i for i in range(a + 1, b) if i not in t[2:8]]
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]