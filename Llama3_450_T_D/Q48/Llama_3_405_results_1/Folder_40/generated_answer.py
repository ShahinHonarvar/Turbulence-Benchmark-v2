def return_binary_or_hexa(t):
    a, _, _, b = t
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]