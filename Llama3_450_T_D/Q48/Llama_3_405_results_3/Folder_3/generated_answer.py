def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[57:88]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]