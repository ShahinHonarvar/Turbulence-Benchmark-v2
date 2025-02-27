def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    s = set(t[275:872])
    sum_missing = sum((i for i in range(a + 1, b) if i not in s))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]