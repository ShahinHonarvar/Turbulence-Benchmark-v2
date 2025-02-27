def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[11:12]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]