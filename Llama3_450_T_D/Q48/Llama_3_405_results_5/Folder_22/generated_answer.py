def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[41:200]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]