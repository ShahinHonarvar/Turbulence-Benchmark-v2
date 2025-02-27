def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    present_set = set(t[:5])
    sum_missing = sum((i for i in range(a + 1, b) if i not in present_set))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]