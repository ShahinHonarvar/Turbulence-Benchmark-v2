def return_binary_or_hexa(t):
    a, b = (t[10], t[28])
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[10:29]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    return ''