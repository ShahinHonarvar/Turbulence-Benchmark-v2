def return_binary_or_hexa(integers):
    a = integers[46]
    b = integers[91]
    sum_missing = sum(set(range(a + 1, b)) - set(integers[47:91]))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]