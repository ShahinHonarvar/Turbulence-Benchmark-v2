def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    lst = list(range(a + 1, b))
    sum_of_missing = sum((i for i in lst if i not in t[11:76]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()