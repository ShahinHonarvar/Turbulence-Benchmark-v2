def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    excluded = set(tup[38:53])
    sum_range = sum((i for i in range(a + 1, b) if i not in excluded))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].upper()