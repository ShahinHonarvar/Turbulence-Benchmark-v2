def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    elements_in_range = set(t[34:78])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in elements_in_range))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]