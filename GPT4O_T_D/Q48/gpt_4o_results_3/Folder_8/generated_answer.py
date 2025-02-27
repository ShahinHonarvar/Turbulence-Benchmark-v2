def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    numbers_in_range = set(t[46:48])
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]