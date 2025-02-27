def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[20:44]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]