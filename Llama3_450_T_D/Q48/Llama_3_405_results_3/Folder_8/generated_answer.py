def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[46:48]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]